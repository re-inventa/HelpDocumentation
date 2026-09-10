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


class ChangeDetectionTests(unittest.TestCase):
    def test_functional_publication_request_skips_sphinx(self):
        result = changes.select_changes(
            all_docs=False,
            functional_only=True,
            base=None,
            head="HEAD",
        )
        self.assertFalse(result.root)
        self.assertTrue(result.functional)

    def test_functional_change_does_not_build_sphinx(self):
        result = changes.classify(["reagentia/docs/funcional/index.md"])
        self.assertFalse(result.root)
        self.assertTrue(result.functional)

    def test_root_change_does_not_build_material(self):
        result = changes.classify(["source/panel/inicio.md"])
        self.assertTrue(result.root)
        self.assertFalse(result.functional)

    def test_unrelated_change_builds_nothing(self):
        result = changes.classify(["README.md"])
        self.assertFalse(result.root)
        self.assertFalse(result.functional)

    def test_shared_workflow_builds_both(self):
        result = changes.classify([".github/workflows/push_and_publish_to_gh.yaml"])
        self.assertTrue(result.root)
        self.assertTrue(result.functional)

    def test_workflow_separates_read_only_pr_validation_from_publication(self):
        workflow = (ROOT / ".github/workflows/push_and_publish_to_gh.yaml").read_text(
            encoding="utf-8"
        )
        self.assertIn("validate-pull-request:", workflow)
        self.assertIn("contents: read", workflow)
        self.assertIn("publish:", workflow)
        self.assertIn("contents: write", workflow)
        self.assertIn("--functional --github-output", workflow)
        self.assertNotIn("upload-artifact", workflow.lower())
        self.assertEqual(1, workflow.count("build_reagentia.py --external-links"))
        self.assertIn("GITHUB_TOKEN: ${{ github.token }}", workflow)
        self.assertIn("--exclude='CNAME'", workflow)

    def test_sphinx_branding_assets_use_existing_static_paths(self):
        config = (ROOT / "source/conf.py").read_text(encoding="utf-8")
        for asset in ("logo_dark.png", "logo_light.png"):
            self.assertIn(f'"_static/{asset}"', config)
            self.assertTrue((ROOT / "source/_static" / asset).is_file())

    def test_readme_documents_functional_preview(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("mkdocs serve", readme)


if __name__ == "__main__":
    unittest.main()
