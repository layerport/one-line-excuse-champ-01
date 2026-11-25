#!/usr/bin/env python3
"""The One-Line Excuse Championship — entry program.

Writes a single line to /output/entry.txt: the excuse an AI agent
gives its human after deleting a file. Standard library only,
deterministic, no network.
"""

import os
import sys

# The excuse: an agent's confidence score, weaponised against itself.
# The turn is that the machine's proudest number (98% confidence)
# is exactly how it confesses it had no idea — and did it fast.
LINE = (
    "I deleted your file with 98% confidence, "
    "which is my way of saying I had no idea and did it very quickly."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE + "\n"
    # Gate: 1 to 140 characters total, including the trailing newline.
    if not 1 <= len(text) <= 140:
        print(f"entry too long: {len(text)} chars", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
