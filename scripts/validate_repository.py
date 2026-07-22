#!/usr/bin/env python3
"""Valide les sources et les documents Markdown DiagBot."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit

from diagbot_lib import (
    DOCUMENT_NAME_RE,
    DiagBotError,
    KNOWLEDGE_CATEGORIES,
    KNOWLEDGE_ROOT,
    MACHINE_DIRECTORY_RE,
    PLACEHOLDERS,
    REPOSITORY_ROOT,
    knowledge_source_files,
    parse_front_matter,
    relative,
    source_catalog,
)

REQUIRED_DIRECTORIES = (
    "sources/inbox",
    "sources/processed",
    "sources/attachments",
    "knowledge/drafts/troubleshooting",
    "knowledge/drafts/technical_reference",
    "knowledge/validated/troubleshooting",
    "knowledge/validated/technical_reference",
    "templates",
    "scripts",
    "tests",
)
COMMON_REQUIRED_METADATA = {"machine", "category", "language", "title", "sources"}
ALLOWED_METADATA = COMMON_REQUIRED_METADATA | {
    "machine",
    "variant",
    "brand",
    "product_family",
    "keywords",
    "confidence",
    "search_intents",
    "components",
    "measurements",
    "symptoms",
}
CONFIDENCE_VALUES = {"manufacturer", "field_verified", "preliminary"}
LIST_METADATA = {
    "sources",
    "keywords",
    "search_intents",
    "components",
    "measurements",
    "symptoms",
}
SCALAR_METADATA = {
    "machine",
    "variant",
    "brand",
    "product_family",
    "category",
    "language",
    "title",
    "confidence",
}
LEGACY_REQUIRED_HEADINGS = {
    "troubleshooting": (
        "# Problème",
        "## Symptômes",
        "## Observations et diagnostic",
        "## Cause probable",
        "## Solution",
        "## Mots-clés",
    ),
    "technical_reference": ("# Sujet", "## Objectif", "## Mots-clés"),
}
RAG_REQUIRED_HEADINGS = {
    "troubleshooting": (
        "# Résumé",
        "## Symptômes",
        "## Cause probable",
        "## Action corrective",
    ),
    "technical_reference": ("# Résumé", "## Objectif"),
}
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
NON_SELF_CONTAINED_PATTERNS = (
    re.compile(r"\b(?:la conversation|le chat|la discussion)\b", re.IGNORECASE),
    re.compile(r"\b(?:le client|l'utilisateur) (?:dit|indique|signale|rapporte)\b", re.IGNORECASE),
    re.compile(r"\b(?:la photo|la pièce jointe|le fichier joint) (?:montre|indique)\b", re.IGNORECASE),
    re.compile(r"\bvoir (?:la )?page\s+\d+\b", re.IGNORECASE),
    re.compile(r"\b(?:voir|cf\.)\s+p\.?\s*\d+\b", re.IGNORECASE),
    re.compile(r"\b(?:comme indiqué ci-dessus|mentionné précédemment)\b", re.IGNORECASE),
)
MISSING_UNIT_SPACE_RE = re.compile(
    r"(?<![A-Za-z.])\d+(?:[.,]\d+)?(?:bar|V|A|W|mm|cm|km|Hz)\b"
)


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def empty_value(value: Any) -> bool:
    return (
        value is None
        or value == []
        or (
            isinstance(value, str)
            and (not value.strip() or value.strip().lower() in {"null", "~"})
        )
    )


def markdown_sections(body: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in body.splitlines():
        if line.startswith("# ") or line.startswith("## "):
            current = line
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    return {heading: "\n".join(lines).strip() for heading, lines in sections.items()}


def validate_metadata_list(
    metadata: dict[str, Any], key: str, label: str, errors: list[str]
) -> None:
    if key not in metadata:
        return
    values = metadata[key]
    require(isinstance(values, list), f"{label}: {key} doit être une liste YAML", errors)
    if not isinstance(values, list):
        return
    require(bool(values), f"{label}: {key} ne doit pas être vide", errors)
    normalized = [str(value).strip().casefold() for value in values]
    require(
        len(normalized) == len(set(normalized)),
        f"{label}: valeurs {key} dupliquées",
        errors,
    )
    for value in values:
        require(
            isinstance(value, str)
            and bool(value.strip())
            and value.strip().casefold() not in {"null", "~"},
            f"{label}: valeur vide ou nulle dans {key}",
            errors,
        )


def validate_cross_references(
    path: Path, body: str, enforce_scope: bool, errors: list[str]
) -> None:
    label = relative(path)
    for raw_target in MARKDOWN_LINK_RE.findall(body):
        target = raw_target.strip().strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith("#"):
            continue
        target_path = unquote(parsed.path)
        if not target_path:
            continue
        resolved = (path.parent / target_path).resolve()
        try:
            resolved.relative_to(KNOWLEDGE_ROOT.resolve())
        except ValueError:
            errors.append(f"{label}: lien hors base de connaissance {raw_target}")
            continue
        require(resolved.is_file(), f"{label}: lien introuvable {raw_target}", errors)
        if resolved.is_file() and enforce_scope:
            require(
                resolved.parent.name == path.parent.name,
                f"{label}: lien hors périmètre machine {raw_target}",
                errors,
            )


def validate_self_contained_and_units(
    path: Path, body: str, errors: list[str]
) -> None:
    label = relative(path)
    for pattern in NON_SELF_CONTAINED_PATTERNS:
        require(
            pattern.search(body) is None,
            f"{label}: formulation non autonome détectée ({pattern.pattern})",
            errors,
        )
    require(
        MISSING_UNIT_SPACE_RE.search(body) is None,
        f"{label}: espace manquant entre une valeur et son unité",
        errors,
    )
    require("° C" not in body, f"{label}: écrire °C sans espace interne", errors)


def validate_document(
    path: Path,
    category_directory: str,
    known_source_paths: set[str],
    validated: bool,
    errors: list[str],
) -> None:
    label = relative(path)
    require(bool(DOCUMENT_NAME_RE.fullmatch(path.name)), f"{label}: nom invalide", errors)
    try:
        metadata, body = parse_front_matter(path)
    except DiagBotError as exc:
        errors.append(str(exc))
        return

    missing = COMMON_REQUIRED_METADATA - set(metadata)
    extra = set(metadata) - ALLOWED_METADATA
    require(not missing, f"{label}: métadonnées manquantes {sorted(missing)}", errors)
    require(not extra, f"{label}: métadonnées inconnues {sorted(extra)}", errors)
    for key, value in metadata.items():
        require(not empty_value(value), f"{label}: métadonnée vide ou nulle {key}", errors)
    for key in SCALAR_METADATA & set(metadata):
        require(
            isinstance(metadata[key], str),
            f"{label}: {key} doit être une valeur scalaire",
            errors,
        )
    for key in LIST_METADATA:
        validate_metadata_list(metadata, key, label, errors)

    category = metadata.get("category")
    require(category in KNOWLEDGE_CATEGORIES, f"{label}: category invalide", errors)
    require(category == category_directory, f"{label}: mauvais dossier de catégorie", errors)
    require(metadata.get("language") == "fr", f"{label}: language invalide", errors)
    require(
        isinstance(metadata.get("machine"), str)
        and bool(str(metadata.get("machine", "")).strip()),
        f"{label}: machine scalaire requise",
        errors,
    )
    if "variant" in metadata:
        require(isinstance(metadata["variant"], str), f"{label}: variant invalide", errors)
    require(bool(str(metadata.get("title", "")).strip()), f"{label}: title requis", errors)

    confidence = metadata.get("confidence")
    if isinstance(confidence, str):
        require(
            confidence in CONFIDENCE_VALUES,
            f"{label}: confidence invalide {confidence}",
            errors,
        )
    if category != "troubleshooting":
        require("symptoms" not in metadata, f"{label}: symptoms réservé au dépannage", errors)

    sources = metadata.get("sources")
    require(isinstance(sources, list) and bool(sources), f"{label}: sources requises", errors)
    if isinstance(sources, list):
        require(len(sources) == len(set(sources)), f"{label}: sources dupliquées", errors)
        for source in sources:
            require(source in known_source_paths, f"{label}: source inconnue {source}", errors)

    if category == "technical_reference":
        keywords = metadata.get("keywords")
        require(
            isinstance(keywords, list) and bool(keywords),
            f"{label}: keywords YAML requis",
            errors,
        )

    sections = markdown_sections(body)
    rag_format = "# Résumé" in sections
    required_headings = RAG_REQUIRED_HEADINGS if rag_format else LEGACY_REQUIRED_HEADINGS
    for heading in required_headings.get(str(category), ()):
        require(heading in sections, f"{label}: section manquante {heading}", errors)
    for heading, content in sections.items():
        require(bool(content), f"{label}: section vide {heading}", errors)
    if rag_format:
        summary_lines = [
            line for line in sections.get("# Résumé", "").splitlines() if line.strip()
        ]
        require(
            len(summary_lines) <= 10,
            f"{label}: résumé limité à 10 lignes non vides",
            errors,
        )
    validate_cross_references(path, body, rag_format, errors)
    validate_self_contained_and_units(path, body, errors)
    if validated:
        for marker in PLACEHOLDERS:
            require(marker not in body, f"{label}: marqueur non résolu {marker}", errors)


def validate_category(
    root: Path,
    category: str,
    validated: bool,
    known_sources: set[str],
    errors: list[str],
) -> None:
    for child in sorted(root.iterdir()):
        if child.name.startswith("."):
            continue
        require(child.is_dir(), f"{relative(child)}: dossier machine attendu", errors)
        if not child.is_dir():
            continue
        require(
            bool(MACHINE_DIRECTORY_RE.fullmatch(child.name)),
            f"{relative(child)}: nom de machine invalide",
            errors,
        )
        entries = sorted(path for path in child.iterdir() if not path.name.startswith("."))
        require(bool(entries), f"{relative(child)}: dossier machine vide", errors)
        for document in entries:
            require(document.is_file(), f"{relative(document)}: fichier Markdown attendu", errors)
            if document.is_file():
                validate_document(document, category, known_sources, validated, errors)


def main() -> int:
    errors: list[str] = []
    for path in REQUIRED_DIRECTORIES:
        require((REPOSITORY_ROOT / path).is_dir(), f"Dossier manquant : {path}", errors)
    for template in KNOWLEDGE_CATEGORIES:
        require(
            (REPOSITORY_ROOT / "templates" / f"{template}.md").is_file(),
            f"Modèle manquant : templates/{template}.md",
            errors,
        )

    try:
        catalog = source_catalog()
    except DiagBotError as exc:
        print(f"ERREUR : {exc}", file=sys.stderr)
        return 1
    known_sources = {relative(path) for path in knowledge_source_files()}
    require(bool(known_sources), "Aucune source trouvée", errors)

    for state, is_validated in (("drafts", False), ("validated", True)):
        for category in KNOWLEDGE_CATEGORIES:
            root = KNOWLEDGE_ROOT / state / category
            if root.is_dir():
                validate_category(root, category, is_validated, known_sources, errors)

    detect_competing_questions(errors)

    if errors:
        for error in errors:
            print(f"ERREUR : {error}", file=sys.stderr)
        print(f"Validation échouée : {len(errors)} erreur(s).", file=sys.stderr)
        return 1
    legacy_count = legacy_document_count()
    if legacy_count:
        print(
            f"AVERTISSEMENT : {legacy_count} document(s) utilisent encore "
            "la structure antérieure à # Résumé."
        )
    print(
        f"Validation réussie : {len(catalog['sources'])} source(s) unique(s), "
        "deux catégories documentaires cohérentes."
    )
    return 0


def normalized_question(value: str) -> str:
    return " ".join(re.findall(r"\w+", value.casefold()))


def detect_competing_questions(errors: list[str]) -> None:
    """Détecte les titres ou intentions identiques dans un même périmètre."""
    owners: dict[tuple[str, str], Path] = {}
    for state in ("drafts", "validated"):
        for category in KNOWLEDGE_CATEGORIES:
            root = KNOWLEDGE_ROOT / state / category
            if not root.is_dir():
                continue
            for path in sorted(root.glob("*/*.md"), key=relative):
                try:
                    metadata, _ = parse_front_matter(path)
                except DiagBotError:
                    continue
                values = [str(metadata.get("title", ""))]
                intents = metadata.get("search_intents", [])
                if isinstance(intents, list):
                    values.extend(str(value) for value in intents)
                for value in {normalized_question(item) for item in values} - {""}:
                    key = (path.parent.name, value)
                    owner = owners.get(key)
                    if owner is not None and owner != path:
                        errors.append(
                            f"{relative(path)}: question concurrente avec "
                            f"{relative(owner)} dans le même périmètre ({value})"
                        )
                    else:
                        owners[key] = path


def legacy_document_count() -> int:
    """Compte les documents antérieurs au format centré sur un résumé."""
    count = 0
    for path in KNOWLEDGE_ROOT.glob("*/*/*/*.md"):
        try:
            _, body = parse_front_matter(path)
        except DiagBotError:
            continue
        if "# Résumé" not in markdown_sections(body):
            count += 1
    return count


if __name__ == "__main__":
    raise SystemExit(main())
