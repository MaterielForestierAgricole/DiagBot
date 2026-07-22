#!/usr/bin/env python3
"""Crée un brouillon Markdown vide à partir du modèle de dépannage."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from diagbot_lib import (
    DOCUMENT_NAME_RE,
    MACHINE_DIRECTORY_RE,
    DiagBotError,
    KNOWLEDGE_ROOT,
    REPOSITORY_ROOT,
    knowledge_source_files,
    optional_metadata_list,
    optional_metadata_line,
    relative,
    yaml_string,
)


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--machine", required=True, help="machine, ex. CS4218")
    parser.add_argument(
        "--folder",
        default="",
        help="dossier machine ; par défaut MACHINE_VARIANT ou MACHINE",
    )
    parser.add_argument("--slug", required=True, help="nom ASCII sans extension")
    parser.add_argument("--title", required=True, help="titre factuel")
    parser.add_argument("--source", action="append", required=True, dest="sources")
    parser.add_argument("--keyword", action="append", dest="keywords")
    parser.add_argument(
        "--confidence",
        choices=("manufacturer", "field_verified", "preliminary"),
        default="",
    )
    parser.add_argument("--search-intent", action="append", dest="search_intents")
    parser.add_argument("--component", action="append", dest="components")
    parser.add_argument("--measurement", action="append", dest="measurements")
    parser.add_argument("--symptom", action="append", dest="symptoms")
    parser.add_argument("--variant", default="")
    parser.add_argument("--brand", default="")
    parser.add_argument("--product-family", default="", dest="product_family")
    return parser.parse_args()


def main() -> int:
    args = arguments()
    try:
        folder = args.folder.strip() or (
            f"{args.machine}_{args.variant}" if args.variant.strip() else args.machine
        )
        if not MACHINE_DIRECTORY_RE.fullmatch(folder):
            raise DiagBotError("Nom de dossier machine invalide.")
        filename = f"{args.slug}.md"
        if not DOCUMENT_NAME_RE.fullmatch(filename):
            raise DiagBotError("Slug invalide : utiliser minuscules, chiffres et tirets.")
        title = args.title.strip()
        if not title:
            raise DiagBotError("Titre requis.")

        known_sources = {relative(path) for path in knowledge_source_files()}
        sources = sorted(set(args.sources))
        unknown = sorted(set(sources) - known_sources)
        if unknown:
            raise DiagBotError(f"Source(s) inconnue(s) : {', '.join(unknown)}")

        machine_directory = KNOWLEDGE_ROOT / "drafts" / "troubleshooting" / folder
        destination = machine_directory / filename
        if destination.exists():
            raise DiagBotError(f"Le document existe déjà : {relative(destination)}")
        machine_directory.mkdir(parents=True, exist_ok=True)

        template = (REPOSITORY_ROOT / "templates" / "troubleshooting.md").read_text(
            encoding="utf-8"
        )
        replacements = {
            "[MACHINE_METADATA]": optional_metadata_line("machine", args.machine),
            "[VARIANT_METADATA]": optional_metadata_line("variant", args.variant),
            "[BRAND_METADATA]": optional_metadata_line("brand", args.brand),
            "[PRODUCT_FAMILY_METADATA]": optional_metadata_line(
                "product_family", args.product_family
            ),
            "[TITLE]": yaml_string(title),
            "[CONFIDENCE_METADATA]": optional_metadata_line(
                "confidence", args.confidence
            ),
            "[SOURCES]": "\n".join(f"  - {yaml_string(source)}" for source in sources),
            "[KEYWORDS_METADATA]": optional_metadata_list("keywords", args.keywords),
            "[SEARCH_INTENTS_METADATA]": optional_metadata_list(
                "search_intents", args.search_intents
            ),
            "[COMPONENTS_METADATA]": optional_metadata_list(
                "components", args.components
            ),
            "[MEASUREMENTS_METADATA]": optional_metadata_list(
                "measurements", args.measurements
            ),
            "[SYMPTOMS_METADATA]": optional_metadata_list("symptoms", args.symptoms),
        }
        body = template
        for marker, value in replacements.items():
            body = body.replace(marker, value)
        destination.write_text(body, encoding="utf-8")
        print(f"Brouillon créé : {relative(destination)}")
        return 0
    except (DiagBotError, OSError) as exc:
        print(f"ERREUR : {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
