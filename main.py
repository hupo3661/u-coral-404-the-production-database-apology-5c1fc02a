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


def main() -> None:
    assert "\n" not in LINE, "entry must be a single line"
    assert len(LINE) <= 200, f"entry is {len(LINE)} chars, over the 200 limit"
    print(LINE)


if __name__ == "__main__":
    main()
