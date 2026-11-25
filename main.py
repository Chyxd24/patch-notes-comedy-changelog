"""Real-Life Patch Notes: The Comedy Changelog.

Writes one fake patch-note line for a real-life bug to /output/entry.txt.
Gate: 1..160 chars, UTF-8, not only whitespace.
Revision: rewrote as a structured function with a named constant.
"""
import os

OUT_DIR = "/output"
LABEL = "v9.9.9 hotfix: confidence now inversely coupled to competence — fixing the bug where they shipped tied together for everyone."


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(LABEL) <= 160, len(LABEL)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w") as fh:
        fh.write(LABEL)


if __name__ == "__main__":
    main()