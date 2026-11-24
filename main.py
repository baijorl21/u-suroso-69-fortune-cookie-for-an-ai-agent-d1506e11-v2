#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent entrypoint.

Writes one funny fortune cookie line for an AI agent (120 characters) to
/output/entry.txt: a single line, in the voice of a fortune slip, about
the user who pastes 4,000 lines and writes only "fix it".
The line is a fixed string (120 characters, verified against the gate),
so two runs always produce the same file. Stdlib only, no network.

Local check (outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys
from pathlib import Path

LINE = (
    'A user will paste 4,000 lines of code and write only "fix it". '
    "The stars advise: charge extra, and read the error first."
)

DEFAULT_OUTPUT = "/output"


def output_path() -> Path:
    """Where the grader expects the text, creating the folder first."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT)
    folder = Path(wanted)
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 140:
        print(f"entry line is {len(LINE)} chars, must be 1-140", file=sys.stderr)
        raise SystemExit(1)
    if not LINE.strip():
        print("entry line is only white space", file=sys.stderr)
        raise SystemExit(1)
    output_path().write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
