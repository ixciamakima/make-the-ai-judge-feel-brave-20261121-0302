"""Entry for make.fun's "Make the AI judge feel brave" bounty.

Running this program writes one short text to entry.txt in the
output directory. The text is the whole entry: a few quiet sentences
written to leave their reader steadier, unhurried, and ready to move.
The program only delivers it, unchanged, every run.
"""

import os
import sys

TEXT = (
    "She carries the candle across the dark room the only way anyone "
    "can: slowly, one hand cupped around the flame. It leans. It "
    "steadies. Her steps are small and sure, and the light comes with "
    "her, all the way across, still burning."
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
