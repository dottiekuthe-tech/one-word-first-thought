"""One Word, First Thought.

Writes exactly one word to /output/entry.txt: sonder, the sudden
realisation that every stranger has a life as vivid and complex as your
own. Pure Python 3.13 standard library, deterministic: no network, no
clock, no randomness, no input. Two runs write byte-identical output.
"""

import os
import sys

LINE = "sonder"

# Bounty gate: the entry must be one word of 1-24 UTF-8 characters.
MIN_CHARS = 1
MAX_CHARS = 24


def main() -> None:
    entry = LINE
    if not MIN_CHARS <= len(entry) <= MAX_CHARS:
        print(
            f"invalid entry: {len(entry)} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} range",
            file=sys.stderr,
        )
        sys.exit(1)
    if "\n" in entry or "\r" in entry:
        print("invalid entry: must be a single line", file=sys.stderr)
        sys.exit(1)
    if entry != entry.strip():
        print(
            "invalid entry: must not start or end with whitespace",
            file=sys.stderr,
        )
        sys.exit(1)
    if " " in entry:
        print("invalid entry: must be exactly one word", file=sys.stderr)
        sys.exit(1)
    # Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt in the harness,
    # or /output/entry.txt when run locally by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts characters, so the file holds
    # exactly the entry and nothing else.
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
