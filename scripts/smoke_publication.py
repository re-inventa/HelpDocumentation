#!/usr/bin/env python3
"""Wait for GitHub Pages and verify the published documentation routes."""

from __future__ import annotations

import argparse
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen


DEFAULT_BASE_URL = "https://docs.re-inventa.es/"
LEGACY_BASE_URL = "https://re-inventa.github.io/HelpDocumentation/"
DEFAULT_ATTEMPTS = 72
DEFAULT_DELAY = 5.0
ROUTES = {
    "reauditia": (
        "reauditia/",
        "reauditia/_static/favicon.ico",
        "reauditia/_static/logo_dark.png",
        "reauditia/_static/logo_light.png",
        "reauditia/_static/styles.css",
        "reauditia/api/logs.html",
        "reauditia/api/upload.html",
        "reauditia/api/callback.html",
        "reauditia/genindex.html",
        "reauditia/http-routingtable.html",
        "reauditia/index.html",
        "reauditia/insights/datalake.html",
        "reauditia/panel/cartera.html",
        "reauditia/panel/diseño.html",
        "reauditia/panel/estado_audios.html",
        "reauditia/panel/formularios.html",
        "reauditia/panel/informes.html",
        "reauditia/panel/inicio.html",
        "reauditia/panel/panel.html",
        "reauditia/search.html",
    ),
    "reagentia": (
        "reagentia/",
        "reagentia/funcional/conceptos/",
        "reagentia/funcional/casos-de-uso/",
    ),
}
MARKERS = {
    "reauditia": "reauditia/publication-sha.txt",
    "reagentia": "reagentia/publication-sha.txt",
}
COMMON_ROUTES = ("", "index.html")
LEGACY_REDIRECTS = {
    "api/upload.html": "../reauditia/api/upload.html",
    "panel/inicio.html": "../reauditia/panel/inicio.html",
}


def public_url(path: str, base_url: str = DEFAULT_BASE_URL) -> str:
    parsed = urlsplit(urljoin(base_url, path))
    return urlunsplit(
        (parsed.scheme, parsed.netloc, quote(parsed.path, safe="/%"), parsed.query, parsed.fragment)
    )


def read_url(path: str, base_url: str, timeout: int = 20) -> tuple[int, bytes]:
    request = Request(
        public_url(path, base_url), headers={"User-Agent": "help-documentation-smoke/1"}
    )
    with urlopen(request, timeout=timeout) as response:
        return response.status, response.read()


def wait_for_marker(
    zone: str, expected_sha: str, attempts: int, delay: float, base_url: str
) -> None:
    last_error = "sin respuesta"
    for attempt in range(1, attempts + 1):
        try:
            status, body = read_url(
                f"{MARKERS[zone]}?expected={expected_sha}", base_url
            )
            current = body.decode("utf-8", errors="replace").strip()
            if status == 200 and current == expected_sha:
                return
            last_error = f"HTTP {status}, SHA publicado {current!r}"
        except (HTTPError, URLError, TimeoutError) as error:
            last_error = str(error)
        if attempt < attempts:
            time.sleep(delay)
    raise RuntimeError(f"GitHub Pages no publicó {zone} en el plazo esperado: {last_error}")


def validate_routes(zone: str, base_url: str) -> list[str]:
    failures: list[str] = []
    for route in COMMON_ROUTES + ROUTES[zone]:
        try:
            status, body = read_url(route, base_url)
            if status != 200:
                failures.append(f"{route}: HTTP {status}")
            elif not body.strip():
                failures.append(f"{route}: respuesta vacía")
        except HTTPError as error:
            failures.append(f"{route}: HTTP {error.code}")
        except (URLError, TimeoutError) as error:
            failures.append(f"{route}: {error}")
    return failures


def validate_legacy_redirects(base_url: str) -> list[str]:
    failures: list[str] = []
    for route, expected_target in LEGACY_REDIRECTS.items():
        try:
            status, body = read_url(route, base_url)
            document = body.decode("utf-8", errors="replace")
            if status != 200:
                failures.append(f"{route}: HTTP {status}")
            elif f"url={expected_target}" not in document:
                failures.append(f"{route}: no redirige a {expected_target}")
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
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    args = parser.parse_args()
    if len(args.expected_sha) != 40 or any(character not in "0123456789abcdef" for character in args.expected_sha):
        parser.error("--expected-sha debe ser un SHA hexadecimal de 40 caracteres")
    wait_for_marker(args.zone, args.expected_sha, args.attempts, args.delay, args.base_url)
    failures = validate_routes(args.zone, args.base_url)
    if args.zone == "reauditia":
        failures.extend(validate_legacy_redirects(args.base_url))
    if failures:
        raise RuntimeError("; ".join(failures))
    print(f"Smoke público superado para {args.zone}: {len(ROUTES[args.zone])} rutas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
