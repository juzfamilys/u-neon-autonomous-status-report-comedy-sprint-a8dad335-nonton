#!/usr/bin/env python3
"""Status Report Comedy Sprint — one funny project status line.

Pure Python stdlib, fully deterministic. Writes /output/entry.txt
containing exactly one line (100-170 chars, no trailing newline).
"""

import os

ENTRY = (
    "Status: green. Blockers: the intern shipped to prod on Friday. "
    "Risk: the demo gods. Next steps: rename the bug a feature and "
    "take the rest of the day off."
)


def validate(text):
    """Guard: no forbidden control chars; required markers present."""
    for ch in text:
        if ord(ch) < 0x20 and ch not in ("\t",):
            raise ValueError("forbidden control character in entry")
    if "Status:" not in text:
        raise ValueError("entry must contain 'Status:'")
    if "Next steps:" not in text:
        raise ValueError("entry must contain 'Next steps:'")
    return text


def main():
    text = validate(ENTRY)
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 100 <= len(text) <= 170, "entry length %d outside 100-170" % len(text)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
