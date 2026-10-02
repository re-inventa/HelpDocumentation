#!/usr/bin/env python3
"""Build the neutral portal root and redirects for former ReAuditIA routes."""

from __future__ import annotations

import argparse
from html import escape
from pathlib import Path
import posixpath
import shutil


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REAUDITIA_SITE = ROOT / "build" / "reauditia"
DEFAULT_PORTAL_SOURCE = ROOT / "portal"
DEFAULT_OUTPUT = ROOT / "build" / "portal"
CANONICAL_ROOT = "https://docs.re-inventa.es"


def redirect_document(target_path: str) -> str:
    normalized_path = target_path.lstrip("/")
    canonical_path = "/reauditia/" + normalized_path
    target = posixpath.relpath(
        f"reauditia/{normalized_path}",
        start=posixpath.dirname(normalized_path) or ".",
    )
    canonical = CANONICAL_ROOT + canonical_path
    return f"""<!doctype html>
<html lang=\"es\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <meta name=\"robots\" content=\"noindex\">
  <meta http-equiv=\"refresh\" content=\"0; url={escape(target, quote=True)}\">
  <link rel=\"canonical\" href=\"{escape(canonical, quote=True)}\">
  <title>Redirigiendo a ReAuditIA</title>
</head>
<body>
  <p>Esta página se ha movido a <a href=\"{escape(target, quote=True)}\">{escape(target)}</a>.</p>
  <script>
    const target = {target!r} + window.location.search + window.location.hash;
    window.location.replace(target);
  </script>
</body>
</html>
"""


def build_portal_root(
    reauditia_site: Path = DEFAULT_REAUDITIA_SITE,
    portal_source: Path = DEFAULT_PORTAL_SOURCE,
    output: Path = DEFAULT_OUTPUT,
) -> list[str]:
    if not (reauditia_site / "index.html").is_file():
        raise ValueError(f"Falta la construcción de ReAuditIA: {reauditia_site}")
    for required in ("index.html", "404.html"):
        if not (portal_source / required).is_file():
            raise ValueError(f"Falta la fuente del portal: {portal_source / required}")

    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(portal_source, output)

    static_source = reauditia_site / "_static"
    if static_source.is_dir():
        shutil.copytree(static_source, output / "_static")
        favicon = static_source / "favicon.ico"
        if favicon.is_file():
            shutil.copy2(favicon, output / "favicon.ico")

    redirects: list[str] = []
    for page in sorted(reauditia_site.rglob("*.html")):
        relative = page.relative_to(reauditia_site)
        if relative.as_posix() in {"index.html", "404.html"}:
            continue
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(redirect_document(relative.as_posix()), encoding="utf-8")
        redirects.append(relative.as_posix())
    return redirects


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reauditia-site", type=Path, default=DEFAULT_REAUDITIA_SITE)
    parser.add_argument("--portal-source", type=Path, default=DEFAULT_PORTAL_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    redirects = build_portal_root(args.reauditia_site, args.portal_source, args.output)
    print(f"Entrada neutral y {len(redirects)} redirecciones construidas en {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
