"""Fortune in a Pot — a one-line fortune for a houseplant.

Entry for the make.fun bounty "Fortune in a Pot"
(u-golden-heron-44-fortune-in-a-pot-ded981e9): a single line, at most
120 characters, telling a houseplant's fortune. The line is written to
/output/entry.txt.
"""

import os

# The fortune itself: 105 characters, counted against the 120 cap.
FORTUNE = (
    "Three new leaves by spring, little fern: the tall window is yours, "
    "and the cat has already been informed."
)

MAX_CHARS = 120
OUTPUT_PATH = "/output/entry.txt"


def fortune_line():
    """Return the fortune, refusing to hand back anything over the cap."""
    line = FORTUNE.strip()
    assert 1 <= len(line) <= MAX_CHARS, f"fortune is {len(line)} chars"
    return line


def main():
    line = fortune_line()
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line)
    # Read it back: what the judge opens must be the fortune, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as fh:
        assert fh.read() == line, "entry.txt does not match the fortune"


if __name__ == "__main__":
    main()
