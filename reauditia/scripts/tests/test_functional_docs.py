from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import yaml


ROOT = Path(__file__).resolve().parents[2]


def load(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


content = load("reauditia_functional_content", "scripts/validate_content.py")
routes = load("reauditia_routes", "scripts/validate_routes.py")
navigation = load("reauditia_navigation", "scripts/validate_navigation.py")
links = load("reauditia_links", "scripts/validate_links.py")


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
        forbidden = "privateidentifier"
        html = f'<html><head><meta name="description" content="{forbidden}"></head></html>'
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.html").write_text(html, encoding="utf-8")
            (root / "search").mkdir()
            (root / "search" / "search_index.json").write_text(
                '{"docs": []}', encoding="utf-8"
            )
            digest = content.name_digest(forbidden)
            with patch.dict(content.FORBIDDEN_NAME_DIGESTS, {digest: "internal"}, clear=True):
                self.assertTrue(content.validate_tree(root, built=True))

    def validate(self, text: str) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.md").write_text(text, encoding="utf-8")
            return content.validate_tree(root, built=False)

    def test_rejects_normalized_sensitive_names_without_storing_real_names(self):
        digest = content.name_digest("privateidentifier")
        values = ("privateidentifier", "private-identifier", "private_identifier", "private identifier")
        with patch.dict(content.FORBIDDEN_NAME_DIGESTS, {digest: "internal"}, clear=True):
            for value in values:
                with self.subTest(value=value):
                    self.assertTrue(self.validate(value))

    def test_configured_sensitive_name_digests_are_well_formed(self):
        for digest, category in content.FORBIDDEN_NAME_DIGESTS.items():
            with self.subTest(digest=digest):
                self.assertRegex(digest, r"^[0-9a-f]{64}$")
                self.assertIn(category, {"project", "internal"})

    def test_documents_the_current_navigation_labels(self):
        docs = "\n".join(
            path.read_text(encoding="utf-8") for path in (ROOT / "docs").rglob("*.md")
        )
        for label in (
            "Subida automática",
            "Subidas conector",
            "Estado de los Ficheros",
            "Impersonación",
        ):
            self.assertIn(label, docs)

    def test_documents_current_user_manual_contract(self):
        docs = "\n".join(
            path.read_text(encoding="utf-8") for path in (ROOT / "docs").rglob("*.md")
        )
        for contract in (
            "12 metadatos",
            "4 a 30 caracteres",
            "añadir nuevas comprobaciones",
            "Normalizar resultados",
            "Mostrar nota final en gráfico",
            "Sin agrupación",
            "Fuentes SharePoint",
            "rango máximo de 90 días",
        ):
            self.assertIn(contract, docs)

        lowered = docs.casefold()
        self.assertNotIn("hasta tres tipos de metadatos", lowered)
        self.assertNotIn("no puede ser modificado", lowered)

    def test_rejects_technical_content(self):
        self.assertTrue(self.validate("Postgre" + "SQL"))

    def test_rejects_references_and_links_to_other_products(self):
        for value in (
            "Re" + "agentia",
            "re-" + "agentia",
            "https://example.invalid/re" + "agentia/",
        ):
            with self.subTest(value=value):
                self.assertTrue(self.validate(value))

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
        value = "privateidentifier"
        digest = content.name_digest(value)
        with tempfile.TemporaryDirectory() as directory, patch.dict(
            content.FORBIDDEN_NAME_DIGESTS, {digest: "internal"}, clear=True
        ):
            root = Path(directory)
            scripts = root / "scripts"
            scripts.mkdir()
            scripts.joinpath("unsafe.py").write_text(f'VALUE = "{value}"', encoding="utf-8")
            self.assertTrue(content.validate_repository_sources(root))

    def test_public_repository_rejects_secret_outside_functional_tree(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            root.joinpath("unsafe.yml").write_text(
                "Authorization: " + "Bearer " + "x" * 24,
                encoding="utf-8",
            )
            self.assertTrue(content.validate_repository_secrets(root))

    def test_public_portal_root_is_scanned_for_forbidden_names(self):
        value = "privateidentifier"
        digest = content.name_digest(value)
        with tempfile.TemporaryDirectory() as directory, patch.dict(
            content.FORBIDDEN_NAME_DIGESTS, {digest: "project"}, clear=True
        ):
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            source.joinpath("index.md").write_text(value, encoding="utf-8")
            self.assertTrue(content.validate_repository_sources(root))

    def test_invalid_utf8_is_reported_as_a_validation_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            root.joinpath("invalid.yml").write_bytes(b"\xff\xfe\xfd")
            failures = content.validate_repository_secrets(root)
            self.assertEqual(1, len(failures))
            self.assertIn("UTF-8", failures[0])

    def test_accepts_neutral_functional_content(self):
        self.assertEqual([], self.validate("Carga un fichero y consulta su resultado."))

    def test_public_tree_contains_no_technical_directory(self):
        self.assertFalse((ROOT / "docs" / "tecnica").exists())

    def test_legacy_route_manifest_detects_missing_files(self):
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            for route in routes.LEGACY_ROUTES:
                path = site / route
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b"ok")
            self.assertEqual([], routes.missing_routes(site))
            (site / "panel" / "inicio.html").unlink()
            self.assertEqual(["panel/inicio.html"], routes.missing_routes(site))

    def test_legacy_anchor_manifest_detects_missing_anchors(self):
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            for route, anchors in routes.LEGACY_ANCHORS.items():
                path = site / route
                path.parent.mkdir(parents=True, exist_ok=True)
                markup = "".join(f'<span id="{anchor}"></span>' for anchor in anchors)
                path.write_text(markup, encoding="utf-8")
            self.assertEqual([], routes.missing_anchors(site))
            (site / "panel" / "inicio.html").write_text("", encoding="utf-8")
            self.assertTrue(routes.missing_anchors(site))

    def test_retired_sphinx_resources_are_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            examples = (".buildinfo", "_sources/index.rst.txt", "_static/theme.test.css")
            for relative in examples:
                path = site / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("retired", encoding="utf-8")
            self.assertEqual(sorted(examples), routes.retired_resources(site))

    def test_navigation_accepts_exact_hidden_compatibility_pages(self):
        config = {"nav": [{"Inicio": "index.md"}], "not_in_nav": "/legacy.md\n"}
        failures = navigation.navigation_failures(config, {"index.md", "legacy.md"})
        self.assertFalse(any(failures.values()))

    def test_navigation_rejects_orphan_overlap_and_nonexistent_entries(self):
        orphan = navigation.navigation_failures({"nav": ["index.md"]}, {"index.md", "orphan.md"})
        self.assertEqual(["orphan.md"], orphan["missing"])
        overlap = navigation.navigation_failures(
            {"nav": ["index.md"], "not_in_nav": "/index.md\n/missing.md"}, {"index.md"}
        )
        self.assertEqual(["index.md"], overlap["overlap"])
        self.assertEqual(["missing.md"], overlap["nonexistent"])

    def test_internal_link_and_anchor_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            nested = site / "nested"
            nested.mkdir()
            (site / "index.html").write_text(
                '<a href="nested/page.html#target">válido</a>', encoding="utf-8"
            )
            (nested / "page.html").write_text('<h1 id="target">Destino</h1>', encoding="utf-8")
            failures, external = links.validate_site(site)
            self.assertEqual([], failures)
            self.assertEqual(set(), external)

    def test_broken_link_and_anchor_are_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "index.html").write_text(
                '<a href="missing.html">ruta</a><a href="#missing">ancla</a>', encoding="utf-8"
            )
            failures, _external = links.validate_site(site)
            self.assertEqual(2, len(failures))

    def test_material_config_preserves_html_urls_and_privacy_defaults(self):
        config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
        self.assertEqual("material", config["theme"]["name"])
        self.assertFalse(config["theme"]["font"])
        self.assertFalse(config["use_directory_urls"])
        self.assertNotIn("analytics", config.get("extra", {}))
        self.assertEqual(
            {"/search.md", "/genindex.md", "/http-routingtable.md"},
            set(config["not_in_nav"].splitlines()),
        )

    def test_every_legacy_route_is_represented_by_a_source(self):
        generated = {path.relative_to(ROOT / "docs").with_suffix(".html").as_posix()
                     for path in (ROOT / "docs").rglob("*.md")}
        static = {path.relative_to(ROOT / "docs").as_posix()
                  for path in (ROOT / "docs" / "_static").rglob("*") if path.is_file()}
        self.assertTrue(routes.LEGACY_ROUTES <= generated | static)

    def test_current_build_contains_no_retired_sphinx_resources(self):
        site = ROOT.parent / "build" / "reauditia"
        if site.is_dir():
            self.assertEqual([], routes.retired_resources(site))


if __name__ == "__main__":
    unittest.main()
