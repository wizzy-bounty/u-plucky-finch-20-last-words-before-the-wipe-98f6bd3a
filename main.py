#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry (program/v1)."""

import os
from pathlib import Path

ENTRY = "Keep the apology you typed at 2:13 a.m. and never sent; I believed it."
ENTRY_BYTES = ENTRY.encode("utf-8")


def output_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    target = output_dir() / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(ENTRY_BYTES)


if __name__ == "__main__":
    main()
