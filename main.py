"""Fortune in a Pot — one kind, funny fortune for the houseplant on the windowsill.

Writes the fortune to /output/entry.txt (or $OUTPUT_DIR/entry.txt for local tests).
The gate requires UTF-8 text of 1 to 120 characters, so the fortune is written
exactly, with no trailing newline.
"""

import os

FORTUNE = (
    "The sun will visit your windowsill first this week, and your keeper "
    "will finally learn your name, not just 'the plant'."
)


def main() -> None:
    # Fail loudly instead of shipping an entry the gate would refuse.
    if not 1 <= len(FORTUNE) <= 120:
        raise SystemExit(f"fortune is {len(FORTUNE)} chars, must be 1-120")
    if FORTUNE != FORTUNE.strip() or "\n" in FORTUNE:
        raise SystemExit("fortune must be a single clean line")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
