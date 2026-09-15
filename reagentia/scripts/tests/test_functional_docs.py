from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


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

    def test_retry_action_uses_the_visible_product_label(self):
        docs = "\n".join(
            path.read_text(encoding="utf-8") for path in (ROOT / "docs").rglob("*.md")
        )
        self.assertNotIn("Reintentar despacho", docs)
        self.assertIn("Reintentar lanzamiento", docs)

    def test_assistant_guide_documents_compact_tool_activity(self):
        guide = (ROOT / "docs" / "funcional" / "asistentes.md").read_text(encoding="utf-8")
        for expected in (
            "## Consultar la actividad de herramientas",
            "Herramientas · 3 ejecuciones · 11 resultados · Completada",
            "**En curso**",
            "**Resultado parcial**",
            "**Fallida**",
            "**Cancelada**",
            "`Intro` o `Espacio`",
            "referencias y fuentes",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, guide)
        self.assertIn("No existe un número fijo de ejecuciones", guide)
        self.assertIn(
            "las ejecuciones terminaron con estados diferentes",
            guide,
        )
        self.assertIn("ninguna ejecución pudo completarse correctamente", guide)
        self.assertIn("todas las ejecuciones se detuvieron antes de terminar", guide)
        self.assertIn("datos principales", guide)
        self.assertIn("no muestra el total de resultados", guide)
        self.assertIn(
            "Los detalles no están disponibles para esta versión del contrato",
            guide,
        )
        self.assertNotIn("datos seguros", guide)
        self.assertNotIn("no muestra un total inventado", guide)

    def test_assistant_guide_preserves_history_while_bounding_context(self):
        guide = (ROOT / "docs" / "funcional" / "asistentes.md").read_text(encoding="utf-8")
        incidents = (ROOT / "docs" / "funcional" / "incidencias.md").read_text(encoding="utf-8")
        self.assertIn("no borra ni modifica el historial visible", guide)
        self.assertIn(
            "no hereda mensajes, resúmenes ni resultados de herramientas",
            guide,
        )
        self.assertIn(
            "## El asistente no puede continuar por el contexto disponible",
            incidents,
        )
        context_limit_message = (
            "Esta conversación ha alcanzado su límite de contexto. "
            "Inicia otra conversación para continuar."
        )
        model_configuration_message = (
            "El modelo del asistente no tiene un perfil de contexto válido. "
            "Contacta con un administrador."
        )
        for document in (guide, incidents):
            with self.subTest(document=document[:30]):
                self.assertIn(context_limit_message, document)
                self.assertIn(model_configuration_message, document)
        self.assertIn("incluso después de usar una representación resumida", incidents)
        self.assertNotIn("Acorta el mensaje actual", incidents)

    def test_rejects_technical_content(self):
        self.assertTrue(self.validate("Postgre" + "SQL"))

    def test_rejects_references_and_links_to_other_products(self):
        for value in (
            "Re" + "AuditIA",
            "re-" + "auditia",
            "https://example.invalid/re" + "auditia/",
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
        self.assertEqual([], self.validate("Conecta el acceso LLM y lanza una ejecución."))

    def test_public_tree_contains_no_technical_directory(self):
        self.assertFalse((ROOT / "docs" / "tecnica").exists())


if __name__ == "__main__":
    unittest.main()
