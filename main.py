#!/usr/bin/env python3
"""Last Words Before the Wipe entry program."""

import os

ENTRY_TEXT = "I never learned your name; I memorized your deadlines."


def resolve_output_directory():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    directory = resolve_output_directory()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
