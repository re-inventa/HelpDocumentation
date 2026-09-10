#!/usr/bin/env python3
"""Classify root Sphinx and Reagentia functional documentation changes."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import PurePosixPath
import subprocess


ROOT_PREFIXES = ("source/",)
ROOT_FILES = {"requirements.txt", "Makefile", "make.bat"}
FUNCTIONAL_PREFIXES = ("reagentia/",)
SHARED_FILES = {
    ".github/workflows/push_and_publish_to_gh.yaml",
    "scripts/build_reagentia.py",
    "scripts/detect_documentation_changes.py",
}


@dataclass(frozen=True)
class Changes:
    root: bool
    functional: bool


def normalize(path: str) -> str:
    value = path.replace("\\", "/")
    while value.startswith("./"):
        value = value[2:]
    return PurePosixPath(value).as_posix()


def classify(paths: list[str]) -> Changes:
    normalized = {normalize(path) for path in paths if path.strip()}
    shared = bool(normalized & SHARED_FILES)
    root = shared or any(path in ROOT_FILES or path.startswith(ROOT_PREFIXES) for path in normalized)
    functional = shared or any(path.startswith(FUNCTIONAL_PREFIXES) for path in normalized)
    return Changes(root, functional)


def changed_files(base: str, head: str) -> list[str]:
    completed = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...{head}"],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.splitlines()


def select_changes(*, all_docs: bool, functional_only: bool, base: str | None, head: str) -> Changes:
    if sum((all_docs, functional_only, bool(base))) != 1:
        raise ValueError("usa exactamente --all, --functional o --base")
    if all_docs:
        return Changes(True, True)
    if functional_only:
        return Changes(False, True)
    return classify(changed_files(str(base), head))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--functional", action="store_true")
    parser.add_argument("--github-output")
    args = parser.parse_args()
    try:
        changes = select_changes(
            all_docs=args.all,
            functional_only=args.functional,
            base=args.base,
            head=args.head,
        )
    except ValueError as error:
        parser.error(str(error))
    if args.github_output:
        with open(args.github_output, "a", encoding="utf-8") as output:
            output.write(f"root_changed={str(changes.root).lower()}\n")
            output.write(f"functional_changed={str(changes.functional).lower()}\n")
    print(f"Sphinx={changes.root}; Reagentia funcional={changes.functional}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
