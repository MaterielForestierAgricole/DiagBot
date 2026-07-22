#!/usr/bin/env python3
"""Inventorie les conversations sans interpréter leur contenu technique."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from diagbot_lib import DiagBotError, REPOSITORY_ROOT, source_catalog, write_json


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="contrôler et résumer sans écrire de catalogue",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="chemin de sortie (par défaut : build/catalog/sources.json)",
    )
    return parser.parse_args()


def main() -> int:
    args = arguments()
    try:
        catalog = source_catalog()
        sources = catalog["sources"]
        occurrences = sum(len(item["paths"]) for item in sources)
        duplicate_groups = sum(len(item["paths"]) > 1 for item in sources)
        print(
            f"{occurrences} fichier(s), {len(sources)} source(s) unique(s), "
            f"{duplicate_groups} groupe(s) de doublons exacts."
        )
        if not sources:
            raise DiagBotError("Aucune source conversationnelle trouvée.")
        if not args.check:
            output = args.output or (
                REPOSITORY_ROOT / "build" / "catalog" / "sources.json"
            )
            if not output.is_absolute():
                output = REPOSITORY_ROOT / output
            write_json(output, catalog)
            print(f"Catalogue écrit : {output}")
        return 0
    except DiagBotError as exc:
        print(f"ERREUR : {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
