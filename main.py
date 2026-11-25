"""Real-Life Patch Notes: The Comedy Changelog.

Writes one fake patch-note line for a real-life bug to /output/entry.txt.
Gate: 1..160 chars, UTF-8, not only whitespace.
Revision: punchline moved to the last few words so the laugh lands on the tail.
"""
import os

OUT_DIR = "/output"
# Patch-note register, real-life bug. The turn now arrives in the last words.
LABEL = "v12.0.1: fixed the bug where a rest day made you tired. Your body will now spend the weekend recharging. Or worrying. Default: worrying."


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(LABEL) <= 160, len(LABEL)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LABEL)
    with open(os.path.join(OUT_DIR, "entry.txt"), encoding="utf-8") as fh:
        landed = fh.read()
    assert landed == LABEL, f"readback mismatch: {landed!r}"
    print(f"wrote {len(landed)} chars")


if __name__ == "__main__":
    main()