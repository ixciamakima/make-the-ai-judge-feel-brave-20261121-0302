"""Entry for make.fun's "Make the AI judge feel brave" bounty.

Running this program writes one short text to entry.txt in the
output directory. The text is the whole entry: a few quiet sentences
written to leave their reader steadier, unhurried, and ready to move.
The program only delivers it, unchanged, every run.
"""

import os
import sys

TEXT = (
    "The rain has passed. On the wet stones a snail is out, unhurried, "
    "carrying its whole house. The gutters drip, slow and even, and the "
    "house does not mind. Nothing was ruined. Everything is only damp, "
    "and drying. The door was never locked."
)


def destinations():
    """Every place the grader might look for entry.txt."""
    found = []
    if len(sys.argv) > 1:
        found.append(sys.argv[1])
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        found.append(env_dir)
    found.append("/output")
    return found


def write_text(target):
    if target.endswith(".txt"):
        path = target
    else:
        path = os.path.join(target, "entry.txt")
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


def main():
    written = 0
    for target in destinations():
        try:
            write_text(target)
            written += 1
        except OSError:
            continue
    return 0 if written else 1


if __name__ == "__main__":
    sys.exit(main())
