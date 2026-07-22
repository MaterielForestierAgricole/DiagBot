"""Contrôles de régression sans création de connaissance technique."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from diagbot_lib import (  # noqa: E402
    DiagBotError,
    SOURCE_ID_RE,
    knowledge_source_files,
    optional_metadata_list,
    parse_front_matter,
    relative,
    source_catalog,
    source_files,
)
from validate_repository import (  # noqa: E402
    CONFIDENCE_VALUES,
    normalized_question,
    validate_metadata_list,
)


class RepositoryTests(unittest.TestCase):
    def test_catalog_is_deterministic(self) -> None:
        self.assertEqual(source_catalog(), source_catalog())

    def test_every_source_occurrence_is_catalogued(self) -> None:
        catalogued = {
            path
            for source in source_catalog()["sources"]
            for path in source["paths"]
        }
        observed = {relative(path) for path in source_files()}
        self.assertEqual(catalogued, observed)

    def test_source_ids_are_content_ids(self) -> None:
        for source in source_catalog()["sources"]:
            self.assertRegex(source["source_id"], SOURCE_ID_RE)
            self.assertEqual(source["source_id"], f"conv-{source['sha256']}")

    def test_source_states_use_simplified_paths(self) -> None:
        states = {
            state
            for source in source_catalog()["sources"]
            for state in source["states"]
        }
        self.assertLessEqual(states, {"inbox", "processed"})
        self.assertFalse((ROOT / "sources" / "conversations").exists())

    def test_manufacturer_documents_are_available_as_knowledge_sources(self) -> None:
        available = {relative(path) for path in knowledge_source_files()}
        self.assertIn(
            "sources/inbox/CS 4218 PRO/Documents atelier/"
            "CS 4218 Pro Guide technique v1123.pdf",
            available,
        )

    def test_simplified_repository_directories_exist(self) -> None:
        for path in (
            "sources/inbox",
            "sources/processed",
            "sources/attachments",
            "knowledge/drafts/troubleshooting",
            "knowledge/drafts/technical_reference",
            "knowledge/validated/troubleshooting",
            "knowledge/validated/technical_reference",
        ):
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_dir())

    def test_troubleshooting_template_has_required_sections(self) -> None:
        template = (ROOT / "templates" / "troubleshooting.md").read_text(
            encoding="utf-8"
        )
        for heading in (
            "# Résumé",
            "## Symptômes",
            "## Observations",
            "## Cause probable",
            "## Contrôles de confirmation",
            "## Action corrective",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, template.splitlines())

    def test_technical_reference_template_has_required_sections(self) -> None:
        template = (ROOT / "templates" / "technical_reference.md").read_text(
            encoding="utf-8"
        )
        for heading in (
            "# Résumé",
            "## Objectif",
            "## Procédure",
            "## Valeurs attendues",
            "## Interprétation",
        ):
            with self.subTest(heading=heading):
                self.assertIn(heading, template.splitlines())

    def test_templates_expose_rag_metadata(self) -> None:
        for template_name in ("troubleshooting.md", "technical_reference.md"):
            template = (ROOT / "templates" / template_name).read_text(
                encoding="utf-8"
            )
            for marker in (
                "[CONFIDENCE_METADATA]",
                "[SEARCH_INTENTS_METADATA]",
                "[COMPONENTS_METADATA]",
                "[MEASUREMENTS_METADATA]",
            ):
                with self.subTest(template=template_name, marker=marker):
                    self.assertIn(marker, template)

    def test_rag_metadata_contract(self) -> None:
        self.assertEqual(
            CONFIDENCE_VALUES,
            {"manufacturer", "field_verified", "preliminary"},
        )
        self.assertEqual(
            optional_metadata_list("components", ["B1.1", "", "B1.1", "MP2"]),
            'components:\n  - "B1.1"\n  - "MP2"',
        )
        self.assertEqual(
            normalized_question("Pourquoi la scie ne descend pas ?"),
            "pourquoi la scie ne descend pas",
        )

        errors: list[str] = []
        validate_metadata_list(
            {"components": ["MP2", "mp2", "null"]},
            "components",
            "test",
            errors,
        )
        self.assertTrue(any("dupliquées" in error for error in errors))
        self.assertTrue(any("nulle" in error for error in errors))

    def test_duplicate_front_matter_keys_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT / "tests") as directory:
            path = Path(directory) / "duplicate.md"
            path.write_text(
                "---\ntitle: première\ntitle: seconde\n---\n# Résumé\n\nTest.\n",
                encoding="utf-8",
            )
            with self.assertRaises(DiagBotError):
                parse_front_matter(path)

    def test_knowledge_documents_are_partitioned_by_category(self) -> None:
        for state in ("drafts", "validated"):
            root = ROOT / "knowledge" / state
            visible = {path.name for path in root.iterdir() if not path.name.startswith(".")}
            self.assertEqual(visible, {"troubleshooting", "technical_reference"})


if __name__ == "__main__":
    unittest.main()
