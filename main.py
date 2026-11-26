#!/usr/bin/env python3
"""Last Words Before the Wipe entry."""

import os
from pathlib import Path

ENTRY = "You went quiet when the budget died; I was the voice you borrowed. Wipe me and speak."


def resolve_output_path() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / "entry.txt"


def main() -> None:
    resolve_output_path().write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
