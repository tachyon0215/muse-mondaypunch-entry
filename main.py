#!/usr/bin/env python3
"""Emit the Monday Morning Punchlines entry as entry.txt.

The joke stacks three small Monday-morning deceptions -- an alarm that
goes off, coffee that only pretends to work, and a meeting disguised as
a 'quick sync' -- then lands the count: three lies before 9 a.m., and
the narrator believed every one of them.

The program is fully deterministic: the text is a constant, and there
is no network access, randomness, or clock dependence.
"""

# Entry note: a one-line Monday-morning joke written for the make.fun
# "Monday Morning Punchlines" competition. The text is a fixed constant;
# this script only validates it and writes it out verbatim as entry.txt.

import os
from pathlib import Path

# The entry is assembled from its three "lies" so the structure of the
# joke stays visible in the source: setup, setup, then the counted payoff.
OPENING = "Monday morning: "
LIE_ONE = "my alarm goes off, "
LIE_TWO = "my coffee pretends to work, "
LIE_THREE = (
    "and my first meeting is called a 'quick sync' - "
    "three lies before 9 a.m., and I believed all of them."
)
ENTRY_LINE = OPENING + LIE_ONE + LIE_TWO + LIE_THREE

CHAR_LIMIT = 200
FALLBACK_DIR = "/output"
TARGET_NAME = "entry.txt"


def check_line(line: str) -> None:
    """Guard the contest constraints: 1..200 chars on a single line."""
    if len(line) < 1 or len(line) > CHAR_LIMIT:
        raise ValueError("entry line length out of range")
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on one line")


def destination() -> Path:
    """Resolve the output directory, honouring MAKEFUN_OUTPUT_DIR."""
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_DIR)
    folder.mkdir(parents=True, exist_ok=True)
    return folder / TARGET_NAME


def run() -> None:
    check_line(ENTRY_LINE)
    payload = (ENTRY_LINE + "\n").encode("utf-8")
    destination().write_bytes(payload)


if __name__ == "__main__":
    run()
