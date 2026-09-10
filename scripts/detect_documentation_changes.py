#!/usr/bin/env python3
"""Classify ReAuditIA and Reagentia public documentation changes."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import PurePosixPath
import subprocess


REAUDITIA_PREFIXES = ("reauditia/",)
REAGENTIA_PREFIXES = ("reagentia/",)
SHARED_FILES = {
    ".github/workflows/push_and_publish_to_gh.yaml",
    "scripts/detect_documentation_changes.py",
    "scripts/smoke_publication.py",
}
REAUDITIA_FILES = {"scripts/build_reauditia.py", "dev.bat"}
REAGENTIA_FILES = {"scripts/build_reagentia.py"}


@dataclass(frozen=True)
class Changes:
    reauditia: bool
    reagentia: bool


def normalize(path: str) -> str:
    value = path.replace("\\", "/")
    while value.startswith("./"):
        value = value[2:]
    return PurePosixPath(value).as_posix()


def classify(paths: list[str]) -> Changes:
    normalized = {normalize(path) for path in paths if path.strip()}
    shared = bool(normalized & SHARED_FILES)
    reauditia = shared or bool(normalized & REAUDITIA_FILES) or any(
        path.startswith(REAUDITIA_PREFIXES) for path in normalized
    )
    reagentia = shared or bool(normalized & REAGENTIA_FILES) or any(
        path.startswith(REAGENTIA_PREFIXES) for path in normalized
    )
    return Changes(reauditia, reagentia)


def changed_files(base: str, head: str) -> list[str]:
    completed = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...{head}"],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.splitlines()


def select_changes(
    *,
    all_docs: bool,
    reauditia_only: bool,
    reagentia_only: bool,
    base: str | None,
    head: str,
) -> Changes:
    if sum((all_docs, reauditia_only, reagentia_only, bool(base))) != 1:
        raise ValueError("usa exactamente --all, --reauditia, --reagentia o --base")
    if all_docs:
        return Changes(True, True)
    if reauditia_only:
        return Changes(True, False)
    if reagentia_only:
        return Changes(False, True)
    return classify(changed_files(str(base), head))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--reauditia", action="store_true")
    parser.add_argument("--reagentia", action="store_true")
    parser.add_argument("--github-output")
    args = parser.parse_args()
    try:
        changes = select_changes(
            all_docs=args.all,
            reauditia_only=args.reauditia,
            reagentia_only=args.reagentia,
            base=args.base,
            head=args.head,
        )
    except ValueError as error:
        parser.error(str(error))
    if args.github_output:
        with open(args.github_output, "a", encoding="utf-8") as output:
            output.write(f"reauditia_changed={str(changes.reauditia).lower()}\n")
            output.write(f"reagentia_changed={str(changes.reagentia).lower()}\n")
    print(f"ReAuditIA={changes.reauditia}; Reagentia={changes.reagentia}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
