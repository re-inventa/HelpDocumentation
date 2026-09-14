#!/usr/bin/env python3
"""Wait for GitHub Pages and verify the published documentation routes."""

from __future__ import annotations

import argparse
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen


BASE_URL = "https://re-inventa.github.io/HelpDocumentation/"
DEFAULT_ATTEMPTS = 72
DEFAULT_DELAY = 5.0
ROUTES = {
    "reauditia": (
        "_static/favicon.ico",
        "_static/logo_dark.png",
        "_static/logo_light.png",
        "_static/styles.css",
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
    ),
    "reagentia": (
        "reagentia/",
        "reagentia/funcional/conceptos/",
        "reagentia/funcional/casos-de-uso/",
    ),
}
MARKERS = {
    "reauditia": "publication-sha.txt",
    "reagentia": "reagentia/publication-sha.txt",
}


def public_url(path: str) -> str:
    parsed = urlsplit(urljoin(BASE_URL, path))
    return urlunsplit(
        (parsed.scheme, parsed.netloc, quote(parsed.path, safe="/%"), parsed.query, parsed.fragment)
    )


def read_url(path: str, timeout: int = 20) -> tuple[int, bytes]:
    request = Request(public_url(path), headers={"User-Agent": "help-documentation-smoke/1"})
    with urlopen(request, timeout=timeout) as response:
        return response.status, response.read()


def wait_for_marker(zone: str, expected_sha: str, attempts: int, delay: float) -> None:
    last_error = "sin respuesta"
    for attempt in range(1, attempts + 1):
        try:
            status, body = read_url(f"{MARKERS[zone]}?expected={expected_sha}")
            current = body.decode("utf-8", errors="replace").strip()
            if status == 200 and current == expected_sha:
                return
            last_error = f"HTTP {status}, SHA publicado {current!r}"
        except (HTTPError, URLError, TimeoutError) as error:
            last_error = str(error)
        if attempt < attempts:
            time.sleep(delay)
    raise RuntimeError(f"GitHub Pages no publicó {zone} en el plazo esperado: {last_error}")


def validate_routes(zone: str) -> list[str]:
    failures: list[str] = []
    for route in ROUTES[zone]:
        try:
            status, body = read_url(route)
            if status != 200:
                failures.append(f"{route}: HTTP {status}")
            elif not body.strip():
                failures.append(f"{route}: respuesta vacía")
        except HTTPError as error:
            failures.append(f"{route}: HTTP {error.code}")
        except (URLError, TimeoutError) as error:
            failures.append(f"{route}: {error}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zone", choices=sorted(ROUTES), required=True)
    parser.add_argument("--expected-sha", required=True)
    parser.add_argument("--attempts", type=int, default=DEFAULT_ATTEMPTS)
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY)
    args = parser.parse_args()
    if len(args.expected_sha) != 40 or any(character not in "0123456789abcdef" for character in args.expected_sha):
        parser.error("--expected-sha debe ser un SHA hexadecimal de 40 caracteres")
    wait_for_marker(args.zone, args.expected_sha, args.attempts, args.delay)
    failures = validate_routes(args.zone)
    if failures:
        raise RuntimeError("; ".join(failures))
    print(f"Smoke público superado para {args.zone}: {len(ROUTES[args.zone])} rutas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
