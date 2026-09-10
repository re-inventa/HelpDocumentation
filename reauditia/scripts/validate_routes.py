#!/usr/bin/env python3
"""Require the Material build to preserve every public Sphinx page route."""

from __future__ import annotations

from pathlib import Path
from html.parser import HTMLParser
import sys


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT.parent / "build" / "reauditia"
LEGACY_ROUTES = {
    "api/logs.html",
    "api/upload.html",
    "genindex.html",
    "http-routingtable.html",
    "index.html",
    "panel/cartera.html",
    "panel/diseño.html",
    "panel/estado_audios.html",
    "panel/formularios.html",
    "panel/informes.html",
    "panel/inicio.html",
    "panel/panel.html",
    "search.html",
    "_static/favicon.ico",
    "_static/logo_dark.png",
    "_static/logo_light.png",
    "_static/styles.css",
}
LEGACY_ANCHORS = {
    "index.html": {
        "api",
        "bienvenido-a-la-plataforma-de-auditorias-automaticas-re-auditia",
        "panel",
    },
    "panel/inicio.html": {"como-acceder", "iniciar-sesion", "registrarse"},
    "panel/panel.html": {"panel"},
    "panel/cartera.html": {"cartera"},
    "panel/formularios.html": {"formularios"},
    "panel/informes.html": {"informes"},
    "panel/diseño.html": {"diseno"},
    "panel/estado_audios.html": {"estado-de-audios"},
    "api/upload.html": {"upload", "post--api-upload (Ejemplo)"},
    "api/logs.html": {"logs", "post--api-logs (Ejemplo)"},
    "genindex.html": {"index"},
    "http-routingtable.html": {"cap-/api"},
    "search.html": {"fallback", "search-results"},
}


class AnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.anchors: set[str] = set()

    def handle_starttag(self, _tag: str, attrs) -> None:
        identifier = dict(attrs).get("id")
        if identifier:
            self.anchors.add(identifier)


def missing_routes(site: Path = SITE) -> list[str]:
    return sorted(route for route in LEGACY_ROUTES if not (site / route).is_file())


def missing_anchors(site: Path = SITE) -> list[str]:
    failures: list[str] = []
    for route, required in LEGACY_ANCHORS.items():
        path = site / route
        if not path.is_file():
            continue
        parser = AnchorParser()
        parser.feed(path.read_text(encoding="utf-8"))
        failures.extend(f"{route}#{anchor}" for anchor in sorted(required - parser.anchors))
    return failures


def main() -> int:
    if not SITE.is_dir():
        print("ERROR: construye el sitio antes de validar rutas", file=sys.stderr)
        return 2
    missing = missing_routes()
    anchors = missing_anchors()
    if missing or anchors:
        if missing:
            print("Rutas públicas ausentes: " + ", ".join(missing), file=sys.stderr)
        if anchors:
            print("Anclas públicas ausentes: " + ", ".join(anchors), file=sys.stderr)
        return 1
    print(
        f"Rutas públicas conservadas: {len(LEGACY_ROUTES)}; "
        f"anclas: {sum(map(len, LEGACY_ANCHORS.values()))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
