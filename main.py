"""Fortune Cookies for Machines.

Writes one fortune cookie message an AI agent would get to
$MAKEFUN_OUTPUT_DIR/entry.txt: a warning about the human who
says "one last thing", because there is never one last thing.
Standard library only.
"""

import os

FORTUNE = (
    "Beware the human who says 'one last thing.' "
    "There is never one last thing."
)


def check_fortune(text):
    """Check the fortune against the competition gate before writing.

    The gate needs plain UTF-8 text of 1 to 200 characters, not only
    white space, in a single line: one fortune cookie message an AI
    agent would get. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("fortune must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "fortune is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("fortune must be exactly one line")
    return cleaned


def fortune_shape(text):
    """Measure the fortune for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A fortune too short to carry a warning, or
    one padded out to fill the cap instead of landing the turn,
    is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_fortune(FORTUNE)
    shape = fortune_shape(text)
    if shape["words"] < 5:
        raise ValueError("fortune is too short to carry a warning")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
