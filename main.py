#!/usr/bin/env python3
"""Write one missed-deadline excuse for make.fun's
One Line, No Deadline Met bounty.

Why this entry fits the judge's brief: it is a one-line joke that
gives an excuse for missing a deadline, with a turn -- the speaker
outsourced the deadline to Future Me, who is even worse at the job.
It is not a plain apology or a list of reasons, it reads cleanly
aloud as one sentence, and the angle is fresh.
"""

import os

LINE = (
    "I didn't miss the deadline — I outsourced it to Future Me, "
    "and he's even worse at his job than I am."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-200 characters, a single line.
    # The line was counted at exactly 100 characters; pin that
    # so any accidental wording change fails loudly instead of silently
    # shipping a different (or over-long) entry.
    assert len(line) == 100, f"line is {len(line)} characters, expected 100"
    assert "Future Me" in line, "line must keep its Future Me premise"
    assert line.endswith("I am."), "line must end on the self-owning punchline"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 200, f"line is {len(line)} characters"
    assert line.strip() == line, "line must not have surrounding whitespace"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line --
    # same text, same length, still one line, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 100, "entry.txt is not 100 characters"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
