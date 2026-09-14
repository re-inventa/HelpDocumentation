#!/usr/bin/env python3
"""Validate the pull-request links declared in the PR body."""

from __future__ import annotations

import os
import re
import sys


ALLOWED_REPOSITORIES = {
    "CallbackRouter",
    "ConectoresRe-auditIA",
    "DbRe-AuditIa",
    "ETL_Reauditia_py",
    "FrontSpeechAnalytics",
    "NewBlobEventTrigger",
    "infra-reagentia",
    "re-agentia",
}
DECLARATION = re.compile(
    r"^[ \t]*Source-PR:[ \t]*([^\n]*?)[ \t]*$",
    re.MULTILINE,
)
SOURCE_URL = re.compile(r"^https://github\.com/re-inventa/([^/]+)/pull/([1-9][0-9]*)$")


def validate(body: str) -> list[str]:
    body = body.replace("\r\n", "\n").replace("\r", "\n")
    values = [match.group(1).strip() for match in DECLARATION.finditer(body)]
    if not values:
        return ["Falta la declaración Source-PR"]
    if any(not value for value in values):
        return ["Source-PR no puede estar vacío"]
    if values == ["none"]:
        return []
    if "none" in values:
        return ["Source-PR: none no se puede combinar con URLs"]

    failures: list[str] = []
    seen: set[str] = set()
    for value in values:
        match = SOURCE_URL.fullmatch(value)
        if not match or match.group(1) not in ALLOWED_REPOSITORIES:
            failures.append(f"Source-PR no válido: {value}")
        elif value in seen:
            failures.append(f"Source-PR duplicado: {value}")
        seen.add(value)
    return failures


def main() -> int:
    failures = validate(os.environ.get("PR_BODY", ""))
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print("Declaración Source-PR válida")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
