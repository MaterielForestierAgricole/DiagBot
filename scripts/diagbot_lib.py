"""Fonctions communes aux outils DiagBot, sans dépendance tierce."""

from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCES_ROOT = REPOSITORY_ROOT / "sources"
KNOWLEDGE_ROOT = REPOSITORY_ROOT / "knowledge"
BUILD_ROOT = REPOSITORY_ROOT / "build"

KNOWLEDGE_CATEGORIES = ("troubleshooting", "technical_reference")

SOURCE_STATES = ("inbox", "processed")
SOURCE_ID_RE = re.compile(r"^conv-[a-f0-9]{64}$")
MACHINE_DIRECTORY_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
DOCUMENT_NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*\.md$")
URL_RE = re.compile(r"https?://[^\s)>]+")
PLACEHOLDERS = ("[À RENSEIGNER", "[NON CONFIRMÉ", "[SOURCE REQUISE")


class DiagBotError(RuntimeError):
    """Erreur contrôlée destinée à être affichée à l'utilisateur."""


def relative(path: Path) -> str:
    return path.resolve().relative_to(REPOSITORY_ROOT.resolve()).as_posix()


def source_state(path: Path) -> str:
    parts = path.relative_to(SOURCES_ROOT).parts
    if not parts or parts[0] not in SOURCE_STATES:
        raise DiagBotError(f"Source hors zone gérée : {relative(path)}")
    return parts[0]


def source_files() -> list[Path]:
    """Retourne les conversations Markdown prises en charge par le catalogue."""
    files: list[Path] = []
    for state in SOURCE_STATES:
        root = SOURCES_ROOT / state
        if root.exists():
            files.extend(path for path in root.rglob("*.md") if path.is_file())
    return sorted(files, key=relative)


def knowledge_source_files() -> list[Path]:
    """Retourne tous les fichiers sources pouvant étayer une connaissance."""
    files: list[Path] = []
    for state in SOURCE_STATES:
        root = SOURCES_ROOT / state
        if root.exists():
            files.extend(
                path
                for path in root.rglob("*")
                if path.is_file() and not path.name.startswith(".")
            )
    return sorted(files, key=relative)


def source_catalog() -> dict[str, Any]:
    """Construit un catalogue déterministe en lisant chaque source entièrement."""
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for path in source_files():
        payload = path.read_bytes()
        try:
            text = payload.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise DiagBotError(
                f"Source non UTF-8 : {relative(path)} ({exc})"
            ) from exc

        digest = hashlib.sha256(payload).hexdigest()
        groups[digest].append(
            {
                "path": relative(path),
                "state": source_state(path),
                "size_bytes": len(payload),
                "observations": {
                    "user_messages": sum(
                        line == "### User" for line in text.splitlines()
                    ),
                    "assistant_messages": sum(
                        line == "### Assistant" for line in text.splitlines()
                    ),
                    "attachment_references": sum(
                        line.startswith("User included image:")
                        for line in text.splitlines()
                    ),
                    "url_references": len(URL_RE.findall(text)),
                },
            }
        )

    sources: list[dict[str, Any]] = []
    for digest in sorted(groups):
        occurrences = groups[digest]
        sources.append(
            {
                "source_id": f"conv-{digest}",
                "sha256": digest,
                "size_bytes": occurrences[0]["size_bytes"],
                "paths": sorted(item["path"] for item in occurrences),
                "states": sorted({item["state"] for item in occurrences}),
                "media_type": "text/markdown",
                "observations": occurrences[0]["observations"],
            }
        )

    return {
        "schema_version": 1,
        "generated_by": "scripts/catalog_sources.py",
        "sources": sources,
    }


def parse_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    """Lit le sous-ensemble YAML simple utilisé par les fiches DiagBot."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise DiagBotError(f"Markdown illisible : {relative(path)} ({exc})") from exc
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise DiagBotError(f"Front matter manquant : {relative(path)}")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise DiagBotError(f"Front matter non fermé : {relative(path)}") from exc

    metadata: dict[str, Any] = {}
    list_key: str | None = None
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and list_key:
            metadata[list_key].append(_unquote(line[4:].strip()))
            continue
        if ":" not in line or line.startswith(" "):
            raise DiagBotError(f"Front matter invalide : {relative(path)}")
        key, raw_value = line.split(":", 1)
        key = key.strip()
        if key in metadata:
            raise DiagBotError(
                f"Clé de front matter dupliquée ({key}) : {relative(path)}"
            )
        value = raw_value.strip()
        if not value:
            metadata[key] = []
            list_key = key
        else:
            metadata[key] = _unquote(value)
            list_key = None
    return metadata, "\n".join(lines[end + 1 :]).lstrip("\n")


def _unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def yaml_string(value: str) -> str:
    """Encode une chaîne dans le sous-ensemble YAML utilisé par le dépôt."""
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def optional_metadata_line(key: str, value: str) -> str:
    value = value.strip()
    return f"{key}: {yaml_string(value)}" if value else ""


def optional_metadata_list(key: str, values: list[str] | None) -> str:
    """Encode une liste YAML facultative, sans valeur vide ni doublon."""
    normalized = sorted({value.strip() for value in values or [] if value.strip()})
    if not normalized:
        return ""
    items = "\n".join(f"  - {yaml_string(value)}" for value in normalized)
    return f"{key}:\n{items}"


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False)
    path.write_text(serialized + "\n", encoding="utf-8")


def ensure_within(path: Path, parent: Path) -> Path:
    resolved = path.resolve()
    try:
        resolved.relative_to(parent.resolve())
    except ValueError as exc:
        raise DiagBotError(f"Chemin hors périmètre autorisé : {path}") from exc
    return resolved
