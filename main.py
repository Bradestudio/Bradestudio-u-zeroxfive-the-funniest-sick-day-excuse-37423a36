"""The Funniest Sick-Day Excuse — make.fun bounty entry.

Writes one line (150 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
deterministic: the same bytes on every run.

The excuse is half believable (food poisoning is a classic sick-day
reason a boss can half believe) and fresh (the poisoning came from
the sender's own cooking, not a restaurant). The laugh lands on the
last three words: the stomach filed a formal complaint against the
chef — and the chef is the sender. One read, one twist, no wasted
words, in the voice of a real person typing a sick-day message.
"""

import os
import sys

ENTRY = (
    "Can't come in today \u2014 I gave myself food poisoning with my "
    "own cooking, and my stomach just filed a formal complaint "
    "against the chef. The chef is me."
)


def main():
    text = ENTRY
    if not text or not text.strip():
        sys.exit("entry text is blank")
    if "\n" in text or "\r" in text:
        sys.exit("entry must be exactly one line")
    if text != text.strip():
        sys.exit("entry must not start or end with whitespace")
    if not 1 <= len(text) <= 200:
        sys.exit("entry must be 1-200 characters, got %d" % len(text))
    if not text.startswith("Can't come in today"):
        sys.exit("entry must open as a sick-day message")
    if not text.endswith("The chef is me."):
        # The twist must land on the last words: the chef is the sender.
        sys.exit("entry must end with the twist that the chef is me")
    if "food poisoning" not in text:
        sys.exit("entry must name the believable reason")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Re-read and verify the file is exactly the gated text, no newline.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("entry.txt does not match the gated text")
    print("wrote %s (%d chars, %d bytes, 1 line)"
          % (path, len(text), len(data)))


if __name__ == "__main__":
    main()
