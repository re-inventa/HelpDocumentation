#!/usr/bin/env python3
"""Validate repository-dispatch requests accepted by the publication workflow."""

from __future__ import annotations

import os
import re
import sys


ALLOWED_REQUESTS = {
    ("reagentia-documentation-updated", "re-inventa/re-agentia", "refs/heads/main"),
    ("reagentia-documentation-updated", "re-inventa/infra-reagentia", "refs/heads/main"),
    ("reauditia-documentation-updated", "re-inventa/FrontSpeechAnalytics", "refs/heads/main"),
    ("reauditia-documentation-updated", "re-inventa/NewBlobEventTrigger", "refs/heads/master"),
    ("reauditia-documentation-updated", "re-inventa/DbRe-AuditIa", "refs/heads/main"),
    ("reauditia-documentation-updated", "re-inventa/ConectoresRe-auditIA", "refs/heads/main"),
    ("reauditia-documentation-updated", "re-inventa/ETL_Reauditia_py", "refs/heads/main"),
    ("reauditia-documentation-updated", "re-inventa/CallbackRouter", "refs/heads/main"),
}
SHA = re.compile(r"^[0-9a-f]{40}$")


def validate(
    event_type: str,
    source_repository: str,
    source_ref: str,
    source_sha: str,
    documentation_sha: str,
) -> list[str]:
    failures: list[str] = []
    if (event_type, source_repository, source_ref) not in ALLOWED_REQUESTS:
        failures.append("Tipo, repositorio o rama de origen no permitidos")
    if not SHA.fullmatch(source_sha):
        failures.append("SHA de origen no válido")
    if not SHA.fullmatch(documentation_sha):
        failures.append("SHA documental no válido")
    return failures


def main() -> int:
    failures = validate(
        os.environ.get("EVENT_TYPE", ""),
        os.environ.get("SOURCE_REPOSITORY", ""),
        os.environ.get("SOURCE_REF", ""),
        os.environ.get("SOURCE_SHA", ""),
        os.environ.get("DOCUMENTATION_SHA", ""),
    )
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print("Solicitud de publicación válida")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
