#!/usr/bin/env python3
"""Build and validate the public functional ReAuditIA site owned by this repo."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
FUNCTIONAL_ROOT = ROOT / "reauditia"


def run(*command: str, cwd: Path = ROOT) -> None:
    print(f"+ {' '.join(command)}")
    subprocess.run(command, cwd=cwd, check=True, env=os.environ.copy())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--external-links", action="store_true")
    parser.add_argument("--responsive", action="store_true")
    args = parser.parse_args()

    required = (
        FUNCTIONAL_ROOT / "mkdocs.yml",
        FUNCTIONAL_ROOT / "requirements-docs.txt",
        FUNCTIONAL_ROOT / "docs" / "index.md",
    )
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise ValueError("Faltan fuentes funcionales: " + ", ".join(missing))

    run(sys.executable, "-m", "unittest", "discover", "-s", "reauditia/scripts/tests", "-v")
    run(sys.executable, "reauditia/scripts/validate_content.py", "--source")
    run(sys.executable, "reauditia/scripts/validate_navigation.py")
    run(sys.executable, "-m", "mkdocs", "build", "--strict", "--config-file", "reauditia/mkdocs.yml")
    run(sys.executable, "reauditia/scripts/validate_content.py", "--site")
    run(sys.executable, "reauditia/scripts/validate_routes.py")
    link_command = [sys.executable, "reauditia/scripts/validate_links.py"]
    if args.external_links:
        link_command.append("--external")
    run(*link_command)
    if args.responsive:
        run(sys.executable, "scripts/validate_responsive.py")
    print(f"Guía funcional construida en {ROOT / 'build' / 'reauditia'}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(2)
