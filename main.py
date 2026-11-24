#!/usr/bin/env python3
"""Two Days of Excuses — entry writer.

Reads entry.txt (one line, 1-200 characters), validates the gate from
RULES.txt, and writes it byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13, standard library only.
"""

import os
import sys
from pathlib import Path

MAX_CHARS = 200


def main() -> int:
    here = Path(__file__).resolve().parent
    src = here / "entry.txt"
    text = src.read_text(encoding="utf-8")
    line = text.strip("\n")
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not line.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= MAX_CHARS:
        print(f"error: entry is {len(line)} chars, must be 1-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # write_bytes: byte-for-byte copy of the validated line, no newline added.
    (out_dir / "entry.txt").write_bytes(line.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
