from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[2]


def load():
    spec = importlib.util.spec_from_file_location(
        "detect_documentation_changes", ROOT / "scripts" / "detect_documentation_changes.py"
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


changes = load()


def load_smoke():
    spec = importlib.util.spec_from_file_location(
        "smoke_publication", ROOT / "scripts" / "smoke_publication.py"
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


smoke = load_smoke()


class ChangeDetectionTests(unittest.TestCase):
    def select(self, *, reauditia=False, reagentia=False, all_docs=False):
        return changes.select_changes(
            all_docs=all_docs,
            reauditia_only=reauditia,
            reagentia_only=reagentia,
            base=None,
            head="HEAD",
        )

    def test_reauditia_dispatch_builds_only_reauditia(self):
        result = self.select(reauditia=True)
        self.assertTrue(result.reauditia)
        self.assertFalse(result.reagentia)

    def test_reagentia_dispatch_builds_only_reagentia(self):
        result = self.select(reagentia=True)
        self.assertFalse(result.reauditia)
        self.assertTrue(result.reagentia)

    def test_reauditia_change_does_not_build_reagentia(self):
        result = changes.classify(["reauditia/docs/panel/inicio.md"])
        self.assertTrue(result.reauditia)
        self.assertFalse(result.reagentia)

    def test_reagentia_change_does_not_build_reauditia(self):
        result = changes.classify(["reagentia/docs/funcional/index.md"])
        self.assertFalse(result.reauditia)
        self.assertTrue(result.reagentia)

    def test_unrelated_change_builds_nothing(self):
        result = changes.classify(["README.md"])
        self.assertFalse(result.reauditia)
        self.assertFalse(result.reagentia)

    def test_shared_workflow_builds_both(self):
        result = changes.classify([".github/workflows/push_and_publish_to_gh.yaml"])
        self.assertTrue(result.reauditia)
        self.assertTrue(result.reagentia)

    def test_shared_smoke_change_builds_both(self):
        result = changes.classify(["scripts/smoke_publication.py"])
        self.assertTrue(result.reauditia)
        self.assertTrue(result.reagentia)

    def test_workflow_separates_validation_from_publication(self):
        workflow = (ROOT / ".github/workflows/push_and_publish_to_gh.yaml").read_text(
            encoding="utf-8"
        )
        self.assertIn("validate-pull-request:", workflow)
        self.assertIn("contents: read", workflow)
        self.assertIn("publish:", workflow)
        self.assertIn("contents: write", workflow)
        self.assertNotIn("upload-artifact", workflow.lower())
        self.assertIn("build_reauditia.py --external-links", workflow)
        self.assertIn("build_reagentia.py --external-links", workflow)
        self.assertIn("--exclude='CNAME'", workflow)
        self.assertIn("--exclude='reagentia/'", workflow)
        self.assertIn("smoke_publication.py --zone reauditia", workflow)
        self.assertIn("smoke_publication.py --zone reagentia", workflow)
        self.assertIn("group: help-documentation-publish", workflow)
        self.assertIn("queue: max", workflow)

    def test_sphinx_is_not_part_of_the_workflow(self):
        workflow = (ROOT / ".github/workflows/push_and_publish_to_gh.yaml").read_text(
            encoding="utf-8"
        ).lower()
        self.assertNotIn("sphinx", workflow)

    def test_sphinx_sources_and_dependencies_are_removed(self):
        self.assertFalse((ROOT / "requirements.txt").exists())
        self.assertFalse((ROOT / "Makefile").exists())
        self.assertFalse((ROOT / "make.bat").exists())
        self.assertFalse(any(path.is_file() for path in (ROOT / "source").rglob("*")))

    def test_dispatch_allowlist_uses_each_default_branch(self):
        workflow = (ROOT / ".github/workflows/push_and_publish_to_gh.yaml").read_text(
            encoding="utf-8"
        )
        allowed = (
            "reauditia-documentation-updated:re-inventa/FrontSpeechAnalytics:refs/heads/main",
            "reauditia-documentation-updated:re-inventa/NewBlobEventTrigger:refs/heads/master",
            "reauditia-documentation-updated:re-inventa/DbRe-AuditIa:refs/heads/main",
            "reauditia-documentation-updated:re-inventa/ConectoresRe-auditIA:refs/heads/main",
            "reauditia-documentation-updated:re-inventa/ETL_Reauditia_py:refs/heads/main",
            "reauditia-documentation-updated:re-inventa/CallbackRouter:refs/heads/main",
        )
        for entry in allowed:
            self.assertEqual(1, workflow.count(entry))

    def test_both_material_zones_pin_the_same_dependencies(self):
        reauditia = (ROOT / "reauditia" / "requirements-docs.txt").read_text(encoding="utf-8")
        reagentia = (ROOT / "reagentia" / "requirements-docs.txt").read_text(encoding="utf-8")
        self.assertEqual(reauditia.strip().splitlines(), reagentia.strip().splitlines())

    def test_readme_documents_both_previews(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("reauditia/mkdocs.yml", readme)
        self.assertIn("reagentia/mkdocs.yml", readme)

    def test_functional_pull_request_template_requires_the_source_pr(self):
        template = (ROOT / ".github" / "pull_request_template.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Source-PR:", template)

    def test_public_smoke_covers_both_zones(self):
        self.assertIn("index.html", smoke.ROUTES["reauditia"])
        self.assertIn("panel/inicio.html", smoke.ROUTES["reauditia"])
        self.assertIn("reagentia/", smoke.ROUTES["reagentia"])
        self.assertEqual("publication-sha.txt", smoke.MARKERS["reauditia"])
        self.assertEqual("reagentia/publication-sha.txt", smoke.MARKERS["reagentia"])


if __name__ == "__main__":
    unittest.main()
