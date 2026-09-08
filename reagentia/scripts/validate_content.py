#!/usr/bin/env python3
"""Reject internal, project-specific and sensitive public documentation."""

from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import sys
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = ROOT.parent
DOCS_SOURCE = ROOT / "docs"
SITE = REPOSITORY_ROOT / "build" / "reagentia"
# The blocked names are stored only as one-way digests: the public repository must not
# contain the names it is designed to reject, even inside its own validation code.
FORBIDDEN_NAME_DIGESTS = {
    "1113b3efce29bef1a55c7d80e1a714ce73ef42872bc9d6e87cbad39adcb7ec58": "project",
    "4f9930f1036b91a923f30abe6699fafecd56801c3039c0f38ce7631fdc1a3afa": "internal",
    "581e01b9d3581e0365fa0940dcac403a343a23a735068c1922dacda3b8c27bcd": "project",
    "90e6d56e1aae9367d608f6210c23977fdce63bc3cb64a372aa44cd5f714fb8d9": "internal",
    "c76d06397352059f79fe6dde0b76fa36ec0ecc6405fd4e3706fd6c700122077a": "project",
    "c8894645eae4bf1bd66d3d58b2c697c8923878849f98717f62124be552e16838": "project",
    "ddb6e01645ad96a9472340d1aafb20bbf0b9eccf90f13383b43a0e2499befb11": "project",
}
NAME_WORD = re.compile(r"[^\W_]+", re.UNICODE)
TECHNICAL_INTERNAL = re.compile(
    r"\b(?:Next\.js|BFF|PostgreSQL|Trigger\.dev|Mastra|Key Vault|Container Apps?|Liquibase|RBAC|OIDC|Bicep|secretRef|fencing|gateway|workers?)\b",
    re.IGNORECASE,
)
UUID = re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b", re.IGNORECASE)
BEARER_VALUE = re.compile(r"authorization\s*:\s*bearer\s+\S+", re.IGNORECASE)
SECRET_VALUE = re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b")
TOKEN_VALUE = re.compile(
    r"\b(?:ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|tr_(?:dev|stg|prod)_[A-Za-z0-9_-]{16,})\b",
    re.IGNORECASE,
)
CONNECTION_SECRET = re.compile(
    r"\b(?:AccountKey|SharedAccessSignature|Password|Pwd)\s*=\s*(?![\"']?[$<{])[\"']?[^\s;<>\"']{8,}",
    re.IGNORECASE,
)
DATABASE_URL_SECRET = re.compile(r"\bpostgres(?:ql)?://[^\s:/@]+:[^\s/@]{4,}@", re.IGNORECASE)
SAS_SIGNATURE = re.compile(r"(?:[?&]|\b)sig=[A-Za-z0-9%+/_=-]{12,}", re.IGNORECASE)
PRIVATE_KEY = re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")
EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
SOURCE_TEXT_SUFFIXES = {
    ".bat", ".cfg", ".cjs", ".css", ".html", ".ini", ".js", ".json",
    ".lock", ".md", ".mjs", ".properties", ".ps1", ".py", ".rst", ".sh",
    ".svg", ".toml", ".ts", ".tsx", ".txt", ".xml", ".yaml", ".yml",
}
BUILT_TEXT_SUFFIXES = {".html", ".json", ".xml", ".txt", ".svg"}
EXCLUDED_DIRECTORIES = {".git", "build", "node_modules", "venv"}


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
            if tag == "meta" and values.get("content"):
                self.parts.append(values["content"])

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
    for current_root, directories, filenames in os.walk(root, followlinks=False):
        current = Path(current_root)
        retained_directories = []
        for name in sorted(directories):
            path = current / name
            if name in EXCLUDED_DIRECTORIES or name.startswith(".venv"):
                continue
            if path.is_symlink():
                yield path, "__SYMLINK__"
            else:
                retained_directories.append(name)
        directories[:] = retained_directories
        for name in sorted(filenames):
            path = current / name
            if path.is_symlink():
                yield path, "__SYMLINK__"
            elif (
                path.suffix.lower() in suffixes
                or name in {"Dockerfile", "Makefile"}
                or name.startswith(".env")
            ):
                yield path, path.read_text(encoding="utf-8", errors="strict")


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def check_pattern(path: Path, text: str, pattern: re.Pattern[str], reason: str, failures: list[str]) -> None:
    for match in pattern.finditer(text):
        failures.append(f"{path}:{line_number(text, match.start())}: {reason}")


def normalized_name(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    return "".join(character for character in decomposed if character.isalnum())


def forbidden_names(text: str):
    words = list(NAME_WORD.finditer(text))
    for index, first in enumerate(words):
        combined = first.group(0)
        for length in range(1, 4):
            if length > 1:
                current_index = index + length - 1
                if current_index >= len(words):
                    break
                previous = words[current_index - 1]
                current = words[current_index]
                separator = text[previous.end():current.start()]
                if not separator or any(character not in " _-\t\r\n" for character in separator):
                    break
                combined += current.group(0)
            digest = hashlib.sha256(normalized_name(combined).encode("utf-8")).hexdigest()
            category = FORBIDDEN_NAME_DIGESTS.get(digest)
            if category:
                yield first.start(), category


def check_forbidden_names(path: Path, text: str, context: str, failures: list[str]) -> None:
    reasons = {
        "project": f"referencia a cliente o proyecto {context}",
        "internal": f"nombre interno {context}",
    }
    for offset, category in forbidden_names(text):
        failures.append(f"{path}:{line_number(text, offset)}: {reasons[category]}")


def validate_tree(root: Path, *, built: bool) -> list[str]:
    failures: list[str] = []
    for path, text in iter_text_files(root, built=built):
        if text == "__SYMLINK__":
            failures.append(f"{path}: enlace simbólico no permitido")
            continue
        content = scannable_text(path, text, built=built)
        check_forbidden_names(path, content, "prohibido en la guía funcional", failures)
        for pattern, reason in (
            (TECHNICAL_INTERNAL, "detalle técnico prohibido en la guía funcional"),
            (BEARER_VALUE, "cabecera bearer con valor"),
            (SECRET_VALUE, "valor con forma de secreto"),
            (TOKEN_VALUE, "token con formato real"),
            (CONNECTION_SECRET, "secreto dentro de una cadena de conexión"),
            (DATABASE_URL_SECRET, "credencial dentro de una URL PostgreSQL"),
            (SAS_SIGNATURE, "firma SAS publicada"),
            (PRIVATE_KEY, "clave privada publicada"),
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
            check_forbidden_names(index_path, searchable, "prohibido en el buscador", failures)
            if TECHNICAL_INTERNAL.search(searchable):
                failures.append(f"{index_path}: detalle técnico en el buscador")
    return failures


def validate_separation() -> list[str]:
    failures: list[str] = []
    if (DOCS_SOURCE / "tecnica").exists():
        failures.append(f"{DOCS_SOURCE / 'tecnica'}: la documentación técnica no puede estar en el portal público")
    allowed_roots = {"funcional", "estado"}
    for directory in DOCS_SOURCE.iterdir():
        if directory.is_dir() and directory.name not in allowed_roots:
            failures.append(f"{directory}: directorio no permitido en la guía funcional")
    return failures


def validate_repository_sources(root: Path = ROOT) -> list[str]:
    """Reject forbidden public names outside the Markdown content tree as well."""
    failures: list[str] = []
    docs_root = root / "docs"
    for path, text in iter_text_files(root, built=False):
        try:
            path.relative_to(docs_root)
            continue
        except ValueError:
            pass
        check_forbidden_names(path, text, "prohibido en fuentes públicas", failures)
    return failures


def validate_repository_secrets(root: Path = REPOSITORY_ROOT) -> list[str]:
    """Scan every maintained text source in the public repository for secret values."""
    failures: list[str] = []
    for path, text in iter_text_files(root, built=False):
        if text == "__SYMLINK__":
            failures.append(f"{path}: enlace simbólico no permitido")
            continue
        for pattern, reason in (
            (BEARER_VALUE, "cabecera bearer con valor"),
            (SECRET_VALUE, "valor con forma de secreto"),
            (TOKEN_VALUE, "token con formato real"),
            (CONNECTION_SECRET, "secreto dentro de una cadena de conexión"),
            (DATABASE_URL_SECRET, "credencial dentro de una URL PostgreSQL"),
            (SAS_SIGNATURE, "firma SAS publicada"),
            (PRIVATE_KEY, "clave privada publicada"),
        ):
            check_pattern(path, text, pattern, reason, failures)
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", action="store_true")
    parser.add_argument("--site", action="store_true")
    args = parser.parse_args()
    if args.source == args.site:
        parser.error("elige exactamente --source o --site")
    target = DOCS_SOURCE if args.source else SITE
    if not target.is_dir():
        print(f"ERROR: no existe {target}", file=sys.stderr)
        return 2
    failures = validate_tree(target, built=args.site)
    if args.source:
        failures.extend(validate_separation())
        failures.extend(validate_repository_sources())
        failures.extend(validate_repository_secrets())
        config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        check_forbidden_names(ROOT / "mkdocs.yml", config, "prohibido en mkdocs.yml", failures)
        check_pattern(
            ROOT / "mkdocs.yml",
            config,
            TECHNICAL_INTERNAL,
            "navegación técnica en mkdocs.yml",
            failures,
        )
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"Contenido funcional {'generado' if args.site else 'fuente'} validado")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
