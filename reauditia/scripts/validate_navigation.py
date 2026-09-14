#!/usr/bin/env python3
"""Require every public Markdown page to be navigated or explicitly hidden."""

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


def hidden_pages(config: dict) -> set[str]:
    raw = config.get("not_in_nav", "")
    if not isinstance(raw, str):
        raise ValueError("not_in_nav debe ser una lista de rutas, una por línea")
    values: set[str] = set()
    for line in raw.splitlines():
        value = line.strip()
        if not value:
            continue
        if any(marker in value for marker in "*?[]"):
            raise ValueError(f"not_in_nav no admite patrones: {value}")
        values.add(value.lstrip("/"))
    return values


def navigation_failures(config: dict, pages: set[str]) -> dict[str, list[str]]:
    nav_pages = {
        Path(value).as_posix()
        for value in flatten_nav(config.get("nav", []))
        if str(value).endswith(".md")
    }
    hidden = hidden_pages(config)
    return {
        "missing": sorted(pages - nav_pages - hidden),
        "nonexistent": sorted((nav_pages | hidden) - pages),
        "overlap": sorted(nav_pages & hidden),
        "technical": sorted(value for value in nav_pages if "tecnica" in value.lower()),
    }


def main() -> int:
    config = yaml.load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"), Loader=NavigationLoader)
    pages = {path.relative_to(ROOT / "docs").as_posix() for path in (ROOT / "docs").rglob("*.md")}
    try:
        failures = navigation_failures(config, pages)
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 1
    if any(failures.values()):
        if failures["missing"]:
            print("Páginas huérfanas: " + ", ".join(failures["missing"]), file=sys.stderr)
        if failures["nonexistent"]:
            print("Entradas inexistentes: " + ", ".join(failures["nonexistent"]), file=sys.stderr)
        if failures["overlap"]:
            print("Páginas visibles y ocultas a la vez: " + ", ".join(failures["overlap"]), file=sys.stderr)
        if failures["technical"]:
            print("Entradas técnicas prohibidas: " + ", ".join(failures["technical"]), file=sys.stderr)
        return 1
    print(f"Navegación funcional validada: {len(pages)} páginas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
