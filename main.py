#!/usr/bin/env python3
"""Delete one word from the dictionary forever.

The bounty asks for a single word: the one word we would erase from
the dictionary for good, with nothing else attached. The grader runs
this program and reads /output/entry.txt, so the whole entry is the
word this script writes there.

The pick: Wednesday.

Why this word, in one breath: it is spelled nothing like it sounds
(Wed-nes-day, said "wenz-day"), and erasing it deletes the middle of
the week itself -- Tuesday would fall straight into Thursday, no hump
day, no midweek at all. The joke is in the word alone: a real word
every reader knows, a spelling nobody trusts, and a hole in the
calendar where it used to sit.
"""

import os

WORD = "Wednesday"
OUTPUT_PATH = "/output/entry.txt"


def pick_word() -> str:
    """Return the single word to erase, checked to be exactly one word."""
    word = WORD.strip()
    if not word.isalpha() or " " in word:
        raise ValueError("entry must be exactly one word")
    return word


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(pick_word())


if __name__ == "__main__":
    main()
