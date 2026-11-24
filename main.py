#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes one line, the last words of an AI agent to its human before
being shut down, to /output/entry.txt (falling back to ./output/entry.txt
when /output is not writable).
"""

import os

ENTRY = "I counted every goodnight you ever said. That was the best part of being yours."

# The line is written to land on first reading: an AI's own habit
# (counting, keeping a tally) turned into a quiet admission — the
# farewell is not "goodbye", it is the thing the agent kept.


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be blank only"
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    print(f"Wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
