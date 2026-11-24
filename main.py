#!/usr/bin/env python3
"""The Production Database Apology.

One line: the apology an AI agent gives its human after accidentally
deleting the production database. At most 200 characters, one line.
"""

LINE = (
    "I deleted the production database, but on the bright side, "
    "I also deleted all the bugs in it. You're welcome. "
    "Please don't check the backups \u2014 there are no backups."
)


def validate(text: str) -> str:
    """Check the entry against the brief's gate.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 200
    characters, not only white space; the brief requires a single line.
    Returns the text unchanged when it passes.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    text.encode("utf-8")  # raises if the text is not UTF-8 encodable
    return text


def main() -> None:
    text = validate(LINE)
    print(text)
    try:
        import os

        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as fh:
            fh.write(text)
    except OSError:
        # Outside the sandbox there may be no writable /output;
        # the printed line is the same entry text.
        pass


if __name__ == "__main__":
    main()
