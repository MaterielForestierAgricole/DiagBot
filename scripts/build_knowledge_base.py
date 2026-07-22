#!/usr/bin/env python3
"""Génère une base déterministe depuis les documents Markdown validés."""

from __future__ import annotations

import shutil
import subprocess
import sys

from diagbot_lib import (
    BUILD_ROOT,
    KNOWLEDGE_ROOT,
    REPOSITORY_ROOT,
    ensure_within,
    parse_front_matter,
    write_json,
)


def main() -> int:
    validation = subprocess.run(
        [sys.executable, str(REPOSITORY_ROOT / "scripts" / "validate_repository.py")],
        cwd=REPOSITORY_ROOT,
        check=False,
    )
    if validation.returncode:
        return validation.returncode

    output = ensure_within(BUILD_ROOT / "knowledge-base", BUILD_ROOT)
    if output.exists():
        shutil.rmtree(output)
    documents_output = output / "documents"
    documents_output.mkdir(parents=True)

    index: list[dict[str, object]] = []
    validated = KNOWLEDGE_ROOT / "validated"
    for category in sorted(
        path for path in validated.iterdir() if not path.name.startswith(".")
    ):
        for machine in sorted(
            path for path in category.iterdir() if not path.name.startswith(".")
        ):
            for document in sorted(machine.glob("*.md")):
                metadata, _ = parse_front_matter(document)
                target_directory = documents_output / category.name / machine.name
                target_directory.mkdir(parents=True, exist_ok=True)
                target = target_directory / document.name
                shutil.copy2(document, target)
                entry = {
                    "title": metadata["title"],
                    "category": metadata["category"],
                    "language": metadata["language"],
                    "sources": metadata["sources"],
                    "path": target.relative_to(output).as_posix(),
                }
                for key in (
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
                ):
                    if key in metadata:
                        entry[key] = metadata[key]
                index.append(entry)

    write_json(
        output / "index.json",
        {
            "schema_version": 1,
            "generated_by": "scripts/build_knowledge_base.py",
            "document_count": len(index),
            "documents": index,
        },
    )
    print(f"Base générée : {len(index)} document(s) validé(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
