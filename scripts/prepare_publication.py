#!/usr/bin/env python3
"""Prepare the gh-pages worktree while preserving independent zones and CNAME."""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil


CUSTOM_DOMAIN = "docs.re-inventa.es"
PRESERVED_ROOT_ENTRIES = {".git", ".nojekyll", "CNAME", "reauditia", "reagentia"}


def remove_path(path: Path) -> None:
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink()


def sync_tree(source: Path, destination: Path) -> None:
    if not source.is_dir():
        raise ValueError(f"No existe la salida que se debe publicar: {source}")
    if destination.exists():
        remove_path(destination)
    shutil.copytree(source, destination)


def validate_cname(publish_dir: Path) -> None:
    cname = publish_dir / "CNAME"
    if cname.exists() and cname.read_text(encoding="utf-8").strip() != CUSTOM_DOMAIN:
        raise ValueError(f"CNAME inesperado en {cname}; se esperaba {CUSTOM_DOMAIN}")


def clean_managed_root(publish_dir: Path) -> None:
    for entry in publish_dir.iterdir():
        if entry.name not in PRESERVED_ROOT_ENTRIES:
            remove_path(entry)


def prepare_publication(
    *,
    publish_dir: Path,
    published_sha: str,
    reauditia_changed: bool,
    reagentia_changed: bool,
    reauditia_build: Path,
    reagentia_build: Path,
    portal_build: Path,
) -> None:
    if len(published_sha) != 40 or any(c not in "0123456789abcdef" for c in published_sha):
        raise ValueError("published_sha debe ser un SHA hexadecimal de 40 caracteres")
    if not publish_dir.is_dir():
        raise ValueError(f"No existe el checkout de gh-pages: {publish_dir}")
    validate_cname(publish_dir)

    if reauditia_changed:
        (reauditia_build / "publication-sha.txt").write_text(
            published_sha + "\n", encoding="utf-8"
        )
        sync_tree(reauditia_build, publish_dir / "reauditia")
        clean_managed_root(publish_dir)
        for item in portal_build.iterdir():
            target = publish_dir / item.name
            if target.exists():
                remove_path(target)
            if item.is_dir():
                shutil.copytree(item, target)
            else:
                shutil.copy2(item, target)

    if reagentia_changed:
        (reagentia_build / "publication-sha.txt").write_text(
            published_sha + "\n", encoding="utf-8"
        )
        sync_tree(reagentia_build, publish_dir / "reagentia")

    (publish_dir / ".nojekyll").touch()
    validate_cname(publish_dir)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish-dir", type=Path, required=True)
    parser.add_argument("--published-sha", required=True)
    parser.add_argument("--reauditia", action="store_true")
    parser.add_argument("--reagentia", action="store_true")
    parser.add_argument("--reauditia-build", type=Path, default=Path("build/reauditia"))
    parser.add_argument("--reagentia-build", type=Path, default=Path("build/reagentia"))
    parser.add_argument("--portal-build", type=Path, default=Path("build/portal"))
    args = parser.parse_args()
    if not args.reauditia and not args.reagentia:
        parser.error("indica al menos --reauditia o --reagentia")
    prepare_publication(
        publish_dir=args.publish_dir,
        published_sha=args.published_sha,
        reauditia_changed=args.reauditia,
        reagentia_changed=args.reagentia,
        reauditia_build=args.reauditia_build,
        reagentia_build=args.reagentia_build,
        portal_build=args.portal_build,
    )
    print("Publicación preparada sin perder la otra zona, la entrada raíz ni el CNAME")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
