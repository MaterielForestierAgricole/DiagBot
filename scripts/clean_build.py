#!/usr/bin/env python3
"""Supprime exclusivement les artefacts reconstructibles sous build/."""

from __future__ import annotations

import shutil

from diagbot_lib import BUILD_ROOT, ensure_within


def main() -> int:
    build = BUILD_ROOT.resolve()
    build.mkdir(exist_ok=True)
    for child in build.iterdir():
        if child.name == ".gitkeep":
            continue
        target = ensure_within(child, build)
        if target.is_dir():
            shutil.rmtree(target)
        else:
            target.unlink()
    print("Artefacts générés supprimés.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
