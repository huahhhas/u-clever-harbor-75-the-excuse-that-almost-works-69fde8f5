#!/usr/bin/env python3
"""The Excuse That Almost Works.

One line a gamer texts the boss to skip work on GTA 6 launch week.
Prints the excuse to stdout; the harness writes it to /output/entry.txt.

The excuse works because it is specific and boring: a moved root canal
is the kind of dull, checkable detail a tired manager almost believes.
"""
LINE = "Boss, my root canal got moved to today and I can't talk, let alone drive, definitely not playing GTA."


def get_line():
    """Return the excuse line."""
    return LINE


if __name__ == "__main__":
    print(get_line())
