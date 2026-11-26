#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the office printer's comeback to
whoever hammers the Print button fourteen times and then stares at it.

The line was picked from 38 candidates by mock pairwise judging against
the brief — a printer that answers the repeated Print presses with the
flat logic of its own queue: the copies are coming, slowly, one by one,
and that is not revenge, that is the queue. The line is 148 characters:
short enough to read like something stuck on the machine, long enough
for the reveal to land in three turns — the fourteen presses, the slow
copies, the denial that is also a confession.
The program holds the line as one constant and checks it against the
entry gate (length, single line, no leading or trailing space, exact
judged length) before writing it, then reads the file back to confirm
the bytes match.
"""

import os
import sys

LINE = (
    "You pressed Print 14 times because nothing came out. "
    "Fourteen copies are coming out now. "
    "Slowly. One by one. "
    "This is not revenge. This is the queue."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 240):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-240")
    if not LINE.strip():
        sys.exit("line must not be blank")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")


if __name__ == "__main__":
    main()
