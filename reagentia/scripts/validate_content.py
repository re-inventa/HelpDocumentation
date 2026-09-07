#!/usr/bin/env python3
"""Reject internal, project-specific and sensitive public documentation."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = ROOT.parent
SOURCE = ROOT / "docs"
SITE = REPOSITORY_ROOT / "build" / "reagentia"
PROJECT_SPECIFIC = re.compile(r"\b(?:igap(?:e)?|ig300c|subvenci(?:o|ó)n(?:es)?)\b", re.IGNORECASE)
FUNCTIONAL_INTERNAL = re.compile(r"\bcli[\s_-]*proxy(?:api)?\b", re.IGNORECASE)
TECHNICAL_INTERNAL = re.compile(
    r"\b(?:Next\.js|BFF|PostgreSQL|Trigger\.dev|Mastra|Key Vault|Container Apps?|Liquibase|RBAC|OIDC|Bicep|secretRef|fencing|gateway|workers?)\b",
    re.IGNORECASE,
)
UUID = re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b", re.IGNORECASE)
BEARER_VALUE = re.compile(r"authorization\s*:\s*bearer\s+\S+", re.IGNORECASE)
SECRET_VALUE = re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b")
EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
SOURCE_TEXT_SUFFIXES = {".md", ".html", ".json", ".xml", ".yml", ".yaml", ".txt", ".css", ".js", ".svg"}
BUILT_TEXT_SUFFIXES = {".html", ".json", ".xml", ".txt", ".svg"}


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hidden_depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in {"script", "style", "template"}:
            self.hidden_depth += 1
        if not self.hidden_depth:
            values = dict(attrs)
            self.parts.extend(values[key] for key in ("alt", "title") if values.get(key))

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "template"} and self.hidden_depth:
            self.hidden_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.hidden_depth:
            self.parts.append(data)


def scannable_text(path: Path, text: str, *, built: bool) -> str:
    if not built or path.suffix.lower() != ".html":
        return text
    parser = VisibleTextParser()
    parser.feed(text)
    return "\n".join(parser.parts)


def iter_text_files(root: Path, *, built: bool):
    suffixes = BUILT_TEXT_SUFFIXES if built else SOURCE_TEXT_SUFFIXES
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            yield path, "__SYMLINK__"
        elif path.is_file() and path.suffix.lower() in suffixes:
            yield path, path.read_text(encoding="utf-8", errors="strict")


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def check_pattern(path: Path, text: str, pattern: re.Pattern[str], reason: str, failures: list[str]) -> None:
    for match in pattern.finditer(text):
        failures.append(f"{path}:{line_number(text, match.start())}: {reason}")


def validate_tree(root: Path, *, built: bool) -> list[str]:
    failures: list[str] = []
    for path, text in iter_text_files(root, built=built):
        if text == "__SYMLINK__":
            failures.append(f"{path}: enlace simbólico no permitido")
            continue
        content = scannable_text(path, text, built=built)
        for pattern, reason in (
            (PROJECT_SPECIFIC, "referencia a cliente o proyecto concreto"),
            (FUNCTIONAL_INTERNAL, "nombre interno prohibido en la guía funcional"),
            (TECHNICAL_INTERNAL, "detalle técnico prohibido en la guía funcional"),
            (BEARER_VALUE, "cabecera bearer con valor"),
            (SECRET_VALUE, "valor con forma de secreto"),
            (UUID, "UUID técnico publicado"),
        ):
            check_pattern(path, content, pattern, reason, failures)
        for match in EMAIL.finditer(content):
            if not match.group(0).lower().endswith("@example.invalid"):
                failures.append(f"{path}:{line_number(content, match.start())}: correo no sintético")

    if built:
        index_path = root / "search" / "search_index.json"
        if not index_path.is_file():
            failures.append(f"{index_path}: índice de búsqueda ausente")
        else:
            payload = json.loads(index_path.read_text(encoding="utf-8"))
            searchable = "\n".join(
                f"{entry.get('title', '')}\n{entry.get('text', '')}" for entry in payload.get("docs", [])
            )
            for pattern, reason in (
                (PROJECT_SPECIFIC, "término de cliente o proyecto en el buscador"),
                (FUNCTIONAL_INTERNAL, "nombre interno en el buscador"),
                (TECHNICAL_INTERNAL, "detalle técnico en el buscador"),
            ):
                if pattern.search(searchable):
                    failures.append(f"{index_path}: {reason}")
    return failures


def validate_separation() -> list[str]:
    failures: list[str] = []
    if (SOURCE / "tecnica").exists():
        failures.append(f"{SOURCE / 'tecnica'}: la documentación técnica no puede estar en el portal público")
    allowed_roots = {"funcional", "estado"}
    for directory in SOURCE.iterdir():
        if directory.is_dir() and directory.name not in allowed_roots:
            failures.append(f"{directory}: directorio no permitido en la guía funcional")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", action="store_true")
    parser.add_argument("--site", action="store_true")
    args = parser.parse_args()
    if args.source == args.site:
        parser.error("elige exactamente --source o --site")
    target = SOURCE if args.source else SITE
    if not target.is_dir():
        print(f"ERROR: no existe {target}", file=sys.stderr)
        return 2
    failures = validate_tree(target, built=args.site)
    if args.source:
        failures.extend(validate_separation())
        config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        for pattern, reason in (
            (PROJECT_SPECIFIC, "referencia a cliente o proyecto en mkdocs.yml"),
            (FUNCTIONAL_INTERNAL, "nombre interno en mkdocs.yml"),
            (TECHNICAL_INTERNAL, "navegación técnica en mkdocs.yml"),
        ):
            check_pattern(ROOT / "mkdocs.yml", config, pattern, reason, failures)
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"Contenido funcional {'generado' if args.site else 'fuente'} validado")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
