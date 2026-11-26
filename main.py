#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — entry writer.

Writes the one-sentence out-of-office auto-reply to /output/entry.txt.
Standard library only (os, sys).
"""
import os
import sys

ENTRY = "Thank you for your email \u2014 I am away until Monday, and with 412 unread messages ahead of yours, I will answer the urgent ones first, starting with the one that says this can wait."

MAX_CHARS = 200


def check_length(text):
    """Validate the entry length: at most MAX_CHARS characters."""
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200-char limit" % len(text))


def check_entry(text):
    """Validate the entry: 1-200 chars, one sentence, no edge whitespace."""
    if not text:
        raise ValueError("entry must not be empty")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    check_length(text)
    if not text.endswith("."):
        raise ValueError("entry must end with a period")
    body = text[:-1]
    if any(c in body for c in ".!?"):
        raise ValueError("entry must be a single sentence")
    if any(ord(c) < 32 for c in text):
        raise ValueError("entry must not contain control characters")
    return text


def main():
    check_entry(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote %s (%d chars)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
