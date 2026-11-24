#!/usr/bin/env python3
"""Everyday Wonder — one sentence that makes a small daily moment feel strange and new.

Entry for make.fun bounty
"Everyday Wonder, Two Days to Find the Line"
(u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3).

Pure Python stdlib. Writes exactly one sentence (max 200 characters)
to /output/entry.txt.
"""

import os

SENTENCE = (
    "My kettle clicks off a second early, as if the water peeked at the "
    "future, decided boiling was overrated, and quietly stayed exactly "
    "as it was."
)


def main() -> None:
    sentence = SENTENCE.strip()
    assert sentence, "entry must not be empty"
    assert sentence.count(".") == 1 and sentence.endswith("."), (
        "entry must be exactly one sentence"
    )
    assert 1 <= len(sentence) <= 200, (
        f"entry must be 1-200 characters, got {len(sentence)}"
    )
    out_path = "/output/entry.txt"
    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(sentence + "\n")
    except OSError:
        out_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output", "entry.txt"
        )
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(sentence + "\n")
    print(f"wrote {len(sentence)} characters to {out_path}")
    print(sentence)


if __name__ == "__main__":
    main()
