#!/usr/bin/env python3
"""Validate links in the generated ReAuditIA functional site."""

from __future__ import annotations

import argparse
from functools import lru_cache
from html.parser import HTMLParser
import os
from pathlib import Path
import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT.parent / "build" / "reauditia"
GITHUB_ITEM = re.compile(r"^https://github\.com/([^/]+)/([^/]+)/(issues|pull)/(\d+)(?:[/?#].*)?$")
SITE_URL = re.compile(r"^site_url:\s*(\S+)\s*$", re.MULTILINE)


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links: list[str] = []
        self.anchors: set[str] = set()

    def handle_starttag(self, tag: str, attrs):
        values = dict(attrs)
        if "id" in values:
            self.anchors.add(values["id"])
        if tag in {"a", "link"} and "href" in values:
            self.links.append(values["href"])
        if tag in {"img", "script"} and "src" in values:
            self.links.append(values["src"])


def parse_pages():
    result = {}
    for path in SITE.rglob("*.html"):
        parser = LinkParser()
        parser.feed(path.read_text(encoding="utf-8"))
        result[path.resolve()] = parser
    return result


@lru_cache(maxsize=1)
def configured_site_url() -> str:
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    match = SITE_URL.search(config)
    return match.group(1) if match else ""


def configured_base_path() -> str:
    return urlparse(configured_site_url()).path.rstrip("/")


def is_configured_site_link(link: str) -> bool:
    configured = urlparse(configured_site_url())
    candidate = urlparse(link)
    is_same_site = bool(
        configured.scheme
        and configured.netloc
        and candidate.scheme == configured.scheme
        and candidate.netloc == configured.netloc
        and (candidate.path == configured.path.rstrip("/") or candidate.path.startswith(f"{configured.path.rstrip('/')}/"))
    )
    return is_same_site


def strip_site_prefix(path: str, base_path: str) -> str:
    if not base_path:
        return path
    if path == base_path:
        return "/"
    prefix = f"{base_path}/"
    return path[len(base_path):] if path.startswith(prefix) else path


def resolve_internal(source: Path, link: str) -> tuple[Path, str]:
    parsed = urlparse(link)
    path_part = strip_site_prefix(unquote(parsed.path), configured_base_path())
    if not path_part:
        return source.resolve(), unquote(parsed.fragment)
    target = SITE / path_part.lstrip("/") if path_part.startswith("/") else source.parent / path_part
    if path_part.endswith("/") or not target.suffix:
        target = target / "index.html"
    return target.resolve(), unquote(parsed.fragment)


def github_api_url(url: str) -> str | None:
    match = GITHUB_ITEM.match(url)
    if not match:
        return None
    owner, repo, kind, number = match.groups()
    return f"https://api.github.com/repos/{owner}/{repo}/{'pulls' if kind == 'pull' else 'issues'}/{number}"


def validate_external(url: str, token: str | None) -> str | None:
    checked_url = github_api_url(url) or url
    headers = {"User-Agent": "reauditia-functional-docs-link-checker/1"}
    if checked_url.startswith("https://api.github.com/") and token:
        headers["Authorization"] = f"Bearer {token}"
        headers["Accept"] = "application/vnd.github+json"
    request = Request(checked_url, headers=headers, method="GET")
    last_error = None
    for attempt in range(3):
        try:
            with urlopen(request, timeout=20) as response:
                if 200 <= response.status < 400:
                    return None
                last_error = f"HTTP {response.status}"
        except HTTPError as error:
            last_error = f"HTTP {error.code}"
        except (URLError, TimeoutError) as error:
            last_error = str(error.reason if isinstance(error, URLError) else error)
        if attempt < 2:
            time.sleep(1 + attempt)
    return last_error or "error desconocido"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--external", action="store_true")
    args = parser.parse_args()
    if not SITE.is_dir():
        print("ERROR: construye el sitio antes de validar enlaces", file=sys.stderr)
        return 2

    pages = parse_pages()
    failures: list[str] = []
    external: set[str] = set()
    for source, parsed_page in list(pages.items()):
        for link in parsed_page.links:
            if not link or link.startswith(("mailto:", "tel:", "javascript:", "data:")):
                continue
            parsed = urlparse(link)
            if parsed.scheme in {"http", "https"} and not is_configured_site_link(link):
                external.add(link)
                continue
            target, fragment = resolve_internal(source, link)
            if not target.exists():
                failures.append(f"{source.relative_to(SITE)} -> {link}: destino inexistente")
                continue
            if fragment and target.suffix == ".html":
                target_parser = pages.get(target)
                if target_parser is None:
                    target_parser = LinkParser()
                    target_parser.feed(target.read_text(encoding="utf-8"))
                    pages[target] = target_parser
                if fragment not in target_parser.anchors:
                    failures.append(f"{source.relative_to(SITE)} -> {link}: ancla inexistente")

    if args.external:
        token = os.environ.get("GITHUB_TOKEN")
        for url in sorted(external):
            error = validate_external(url, token)
            if error:
                failures.append(f"{url}: {error}")

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    suffix = " y comprobados" if args.external else ""
    print(f"Enlaces internos validados; externos descubiertos: {len(external)}{suffix}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
