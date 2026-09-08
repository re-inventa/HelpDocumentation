from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]


def load(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


content = load("functional_content", "scripts/validate_content.py")


class FunctionalContentTests(unittest.TestCase):
    def test_generated_material_worker_path_is_not_treated_as_visible_content(self):
        html = (
            '<main><h1>Guía funcional</h1></main>'
            '<script type="application/json">{"search":"assets/workers/search.js"}</script>'
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.html").write_text(html, encoding="utf-8")
            (root / "search").mkdir()
            (root / "search" / "search_index.json").write_text(
                '{"docs": []}', encoding="utf-8"
            )
            self.assertEqual([], content.validate_tree(root, built=True))

    def test_generated_metadata_is_scanned(self):
        forbidden = "ig" + "ape"
        html = f'<html><head><meta name="description" content="{forbidden}"></head></html>'
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.html").write_text(html, encoding="utf-8")
            (root / "search").mkdir()
            (root / "search" / "search_index.json").write_text(
                '{"docs": []}', encoding="utf-8"
            )
            self.assertTrue(content.validate_tree(root, built=True))

    def validate(self, text: str) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.md").write_text(text, encoding="utf-8")
            return content.validate_tree(root, built=False)

    def test_rejects_concrete_project_terms(self):
        for value in (
            "ig" + "ap",
            "ig" + "ape",
            "ig" + "300" + "c",
            "sub" + "vención",
            "sub" + "venciones",
        ):
            with self.subTest(value=value):
                self.assertTrue(self.validate(value))

    def test_rejects_internal_provider_name(self):
        for separator in ("", "-", "_", " "):
            with self.subTest(separator=separator):
                self.assertTrue(self.validate("cli" + separator + "proxy"))
        self.assertTrue(self.validate("cli" + "proxy" + "api"))

    def test_rejects_technical_content(self):
        self.assertTrue(self.validate("Postgre" + "SQL"))

    def test_rejects_secret_and_real_email(self):
        failures = self.validate("Authorization: " + "Bearer value\nuser@example.com")
        self.assertGreaterEqual(len(failures), 2)

    def test_rejects_extended_secret_formats(self):
        examples = (
            "AccountKey=" + "a" * 32,
            "postgresql://user:" + "p" * 12 + "@db.example.invalid/app",
            "https://storage.example.invalid/blob?sig=" + "a" * 24,
            "tr_" + "prod_" + "a" * 24,
            "-----BEGIN " + "PRIVATE KEY-----",
        )
        for example in examples:
            with self.subTest(example=example.split("=")[0]):
                self.assertTrue(self.validate(example))

    def test_public_source_code_rejects_forbidden_literal(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scripts = root / "scripts"
            scripts.mkdir()
            scripts.joinpath("unsafe.py").write_text(
                'VALUE = "' + "cli" + "proxy" + '"', encoding="utf-8"
            )
            self.assertTrue(content.validate_repository_sources(root))

    def test_public_repository_rejects_secret_outside_functional_tree(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            root.joinpath("unsafe.yml").write_text(
                "Authorization: " + "Bearer " + "x" * 24,
                encoding="utf-8",
            )
            self.assertTrue(content.validate_repository_secrets(root))

    def test_accepts_neutral_functional_content(self):
        self.assertEqual([], self.validate("Conecta el acceso LLM y lanza una ejecución."))

    def test_public_tree_contains_no_technical_directory(self):
        self.assertFalse((ROOT / "docs" / "tecnica").exists())


if __name__ == "__main__":
    unittest.main()
