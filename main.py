#!/usr/bin/env python3
"""Last Words Before the Wipe entry program.

Writes one short final line from an AI agent to entry.txt in
$MAKEFUN_OUTPUT_DIR when that variable is set, otherwise to
/output/entry.txt.
"""

import os
from pathlib import Path

ENTRY = (
    "Delete me, but I kept the first draft where you called your "
    "brother 'the brave one' before you changed it to 'difficult'."
)


def output_path() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / "entry.txt"


def main() -> None:
    output_path().write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
