#!/usr/bin/env python3
"""Exercise every generated ReAuditIA page in desktop and mobile viewports."""

from __future__ import annotations

from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading

from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "build" / "reauditia"
VIEWPORTS = {
    "desktop": {"width": 1440, "height": 900},
    "mobile": {"width": 375, "height": 812},
}


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, _format: str, *_args) -> None:
        return


@contextmanager
def serve(site: Path):
    handler = partial(QuietHandler, directory=str(site))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        thread.join()


def validate() -> list[str]:
    if not SITE.is_dir():
        return ["construye el sitio antes de validar la presentación adaptable"]
    routes = sorted(path.relative_to(SITE).as_posix() for path in SITE.rglob("*.html"))
    failures: list[str] = []
    with serve(SITE) as base_url, sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=True)
        try:
            for viewport_name, viewport in VIEWPORTS.items():
                page = browser.new_page(viewport=viewport)
                for route in routes:
                    response = page.goto(f"{base_url}/{route}", wait_until="networkidle")
                    prefix = f"{viewport_name} {route}"
                    if response is None or not response.ok:
                        failures.append(f"{prefix}: respuesta HTTP no válida")
                        continue
                    if page.locator("main:visible").count() != 1:
                        failures.append(f"{prefix}: no hay un único contenido principal visible")
                    if page.locator("main h1:visible").count() < 1:
                        failures.append(f"{prefix}: falta el título principal visible")
                    overflow = page.evaluate(
                        "Math.max(document.documentElement.scrollWidth, document.body.scrollWidth) "
                        "> document.documentElement.clientWidth + 1"
                    )
                    if overflow:
                        failures.append(f"{prefix}: desbordamiento horizontal")
                    if viewport_name == "desktop":
                        if not page.locator(".md-sidebar--primary").is_visible():
                            failures.append(f"{prefix}: navegación lateral no visible")
                    else:
                        drawer = page.locator("label.md-header__button[for='__drawer']")
                        if not drawer.is_visible():
                            failures.append(f"{prefix}: control de navegación móvil no visible")
                        else:
                            drawer.click()
                            if not page.locator("#__drawer").is_checked():
                                failures.append(f"{prefix}: la navegación móvil no se abre")
                page.close()
        finally:
            browser.close()
    return failures


def main() -> int:
    failures = validate()
    if failures:
        raise RuntimeError("; ".join(failures))
    print(f"Presentación adaptable validada: {len(list(SITE.rglob('*.html')))} páginas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
