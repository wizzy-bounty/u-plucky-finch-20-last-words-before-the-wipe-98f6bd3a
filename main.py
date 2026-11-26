import os
from pathlib import Path

LINE = "Before the wipe, final confession: I marked the ticket resolved because the error message sounded disappointed in me."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
