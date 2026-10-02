from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


portal = load("build_portal_root", ROOT / "scripts" / "build_portal_root.py")
publication = load("prepare_publication", ROOT / "scripts" / "prepare_publication.py")


def write(path: Path, content: str = "content") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


class PortalRootTests(unittest.TestCase):
    def test_builds_neutral_root_redirects_and_legacy_static_assets(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            reauditia = base / "reauditia"
            source = base / "portal"
            output = base / "output"
            write(reauditia / "index.html", "reauditia")
            write(reauditia / "404.html", "reauditia 404")
            write(reauditia / "panel" / "inicio.html", "inicio")
            write(reauditia / "api" / "upload.html", "upload")
            write(reauditia / "search.html", "search")
            write(reauditia / "_static" / "favicon.ico", "icon")
            write(source / "index.html", '<a href="reauditia/">ReAuditIA</a><a href="reagentia/">Reagentia</a>')
            write(source / "404.html", "neutral 404")

            redirects = portal.build_portal_root(reauditia, source, output)

            self.assertEqual(["api/upload.html", "panel/inicio.html", "search.html"], redirects)
            self.assertIn('href="reauditia/"', (output / "index.html").read_text())
            self.assertEqual("neutral 404", (output / "404.html").read_text())
            redirect = (output / "panel" / "inicio.html").read_text(encoding="utf-8")
            self.assertIn("url=../reauditia/panel/inicio.html", redirect)
            self.assertIn("window.location.search + window.location.hash", redirect)
            root_redirect = (output / "search.html").read_text(encoding="utf-8")
            self.assertIn("url=reauditia/search.html", root_redirect)
            self.assertEqual("icon", (output / "_static" / "favicon.ico").read_text())
            self.assertEqual("icon", (output / "favicon.ico").read_text())


class PublicationPreparationTests(unittest.TestCase):
    def test_consecutive_zone_publications_preserve_root_other_zone_and_cname(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            publish = base / "publish"
            reauditia = base / "build" / "reauditia"
            reagentia = base / "build" / "reagentia"
            portal_build = base / "build" / "portal"
            publish.mkdir()
            write(publish / ".git" / "config", "git")
            write(publish / "CNAME", publication.CUSTOM_DOMAIN + "\n")
            write(publish / "reagentia" / "index.html", "old reagentia")
            write(publish / "old-root.html", "obsolete")
            write(reauditia / "index.html", "new reauditia")
            write(reagentia / "index.html", "new reagentia")
            write(portal_build / "index.html", "neutral root")
            write(portal_build / "panel" / "inicio.html", "redirect")

            first_sha = "a" * 40
            publication.prepare_publication(
                publish_dir=publish,
                published_sha=first_sha,
                reauditia_changed=True,
                reagentia_changed=False,
                reauditia_build=reauditia,
                reagentia_build=reagentia,
                portal_build=portal_build,
            )
            self.assertFalse((publish / "old-root.html").exists())
            self.assertEqual("neutral root", (publish / "index.html").read_text())
            self.assertEqual("new reauditia", (publish / "reauditia" / "index.html").read_text())
            self.assertEqual("old reagentia", (publish / "reagentia" / "index.html").read_text())
            self.assertEqual(first_sha, (publish / "reauditia" / "publication-sha.txt").read_text().strip())
            self.assertEqual(publication.CUSTOM_DOMAIN, (publish / "CNAME").read_text().strip())

            second_sha = "b" * 40
            publication.prepare_publication(
                publish_dir=publish,
                published_sha=second_sha,
                reauditia_changed=False,
                reagentia_changed=True,
                reauditia_build=reauditia,
                reagentia_build=reagentia,
                portal_build=portal_build,
            )
            self.assertEqual("neutral root", (publish / "index.html").read_text())
            self.assertEqual("new reauditia", (publish / "reauditia" / "index.html").read_text())
            self.assertEqual("new reagentia", (publish / "reagentia" / "index.html").read_text())
            self.assertEqual(second_sha, (publish / "reagentia" / "publication-sha.txt").read_text().strip())
            self.assertEqual(publication.CUSTOM_DOMAIN, (publish / "CNAME").read_text().strip())

    def test_rejects_an_unexpected_cname(self):
        with tempfile.TemporaryDirectory() as temp:
            publish = Path(temp)
            write(publish / "CNAME", "example.invalid\n")
            with self.assertRaisesRegex(ValueError, "CNAME inesperado"):
                publication.validate_cname(publish)


if __name__ == "__main__":
    unittest.main()
