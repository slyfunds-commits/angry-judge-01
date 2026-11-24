#!/usr/bin/env python3
"""Angry Judge R1 entry: writes the keeper rant to /output/entry.txt.

Keeper "Per My Last Email" (186 chars): a funny rant about an everyday
annoyance — the phantom "per my last email". Gate: 1-400 chars UTF-8.
"""
import os

LINE = "\"Per my last email.\" There was no last email. I checked. There was never a first email. \"Per my last email\" is a spell people cast to make their negligence sound like your forgetfulness."


def validate(written):
    # The entry is one rant, nothing else: no trailing newline, gate 1-400.
    assert written == LINE, f"entry.txt mismatch: {written!r}"
    assert not written.endswith("\n"), "entry.txt must not end with a newline"
    assert 1 <= len(LINE) <= 400, f"line is {len(LINE)} chars, outside 1-400"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    validate(written)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
