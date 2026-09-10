#!/usr/bin/env python3
"""Require every public Markdown page to be in the explicit functional navigation."""

from __future__ import annotations

from pathlib import Path
import sys
import yaml


ROOT = Path(__file__).resolve().parents[1]


class NavigationLoader(yaml.SafeLoader):
    pass


NavigationLoader.add_multi_constructor(
    "tag:yaml.org,2002:python/name:",
    lambda _loader, suffix, _node: suffix,
)


def flatten_nav(node):
    if isinstance(node, str):
        yield node
    elif isinstance(node, list):
        for item in node:
            yield from flatten_nav(item)
    elif isinstance(node, dict):
        for value in node.values():
            yield from flatten_nav(value)


def main() -> int:
    config = yaml.load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"), Loader=NavigationLoader)
    nav_pages = {Path(value).as_posix() for value in flatten_nav(config.get("nav", [])) if str(value).endswith(".md")}
    pages = {path.relative_to(ROOT / "docs").as_posix() for path in (ROOT / "docs").rglob("*.md")}
    missing = sorted(pages - nav_pages)
    nonexistent = sorted(nav_pages - pages)
    technical = sorted(value for value in nav_pages if "tecnica" in value.lower())
    if missing or nonexistent or technical:
        if missing:
            print("Páginas huérfanas: " + ", ".join(missing), file=sys.stderr)
        if nonexistent:
            print("Entradas nav inexistentes: " + ", ".join(nonexistent), file=sys.stderr)
        if technical:
            print("Entradas técnicas prohibidas: " + ", ".join(technical), file=sys.stderr)
        return 1
    print(f"Navegación funcional validada: {len(pages)} páginas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
