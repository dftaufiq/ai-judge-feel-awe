#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short text to /output/entry.txt: a quiet scene written to
relax the AI judge reading it, and to dwarf it -- a small human mark
that has outlasted everything built since. Deterministic: the same
text, every run.

The text is built for the judge's brief, in its own order of criteria:
it relaxes by slowing the reader down (short lines, plain words, a
still cave, nothing hurried); the awe comes from the scene itself --
a hand pressed to rock forty thousand years ago, still there while
empires rose and fell -- with no imperative in it, no "look up", no
"be amazed"; the words are plain, concrete and gentle, none that
could be cut; it leaves one thought to return to, that a handprint
outlasts empires; and the Sulawesi cave handprint is a real, specific
image, not a stock wellness phrase or a reworded meditation script.
"""

from pathlib import Path

TEXT = """A handprint on a cave wall in Sulawesi.
Forty thousand years ago, someone pressed a wet palm to the rock and lifted it away.
Empires have risen since, and fallen, and been forgotten.
The hand is still there."""


def main() -> None:
    # The competition gates the entry on 1-280 code points of non-blank
    # text; fail loudly here rather than shipping an entry the grader
    # would reject if the text is ever edited past the gate.
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit(f"text is {len(TEXT)} code points, outside the 1-280 gate")
    if not TEXT.strip():
        raise SystemExit("text is blank")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
