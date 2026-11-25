#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Monday Morning Punchlines": three Monday-morning
lies - the alarm, the coffee pretending to work, and a meeting called a
'quick sync' - counted up in the punchline: three lies before 9 a.m.,
and I believed all of them.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "Monday morning: my alarm goes off, my coffee pretends to work, and my first meeting is called a 'quick sync' - three lies before 9 a.m., and I believed all of them."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
