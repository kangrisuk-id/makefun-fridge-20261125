#!/usr/bin/env python3
"""The 3AM Fridge Text - a make.fun bounty entry.

Writes one line - the text message a smart fridge sends its owner
at 3am - to /output/entry.txt. When the MAKEFUN_OUTPUT_DIR
environment variable is set, the file is written there instead
(for local test runs).

Gate contract (from the bounty kit): /output/entry.txt must be
UTF-8 text of 1 to 140 characters, a single line, not only
whitespace.
"""

import os
import sys

LINE = (
    "You have opened me 4 times since midnight. "
    "The milk and I have agreed: we are not the problem."
)
MAX_CHARS = 140


def validate(line):
    """Raise ValueError unless the line satisfies the gate contract."""
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be blank")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            "line must be 1..%d characters, got %d" % (MAX_CHARS, len(line))
        )
    line.encode("utf-8")  # must be UTF-8 encodable


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
