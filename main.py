"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence, at most 320 characters, to
/output/entry.txt (or the path named by ENTRY_OUT / ENTRY_OUT_DIR
when those are set): a roast of the lawmakers who regulate AI,
crypto and the internet but cannot convert a file to PDF.
"""

import os

MAX_CHARS = 320

# The roast itself: authority set up, then undercut by the file,
# punch landing on the last few words.
ROAST = (
    "The chairman who regulates AI, crypto, and the internet just "
    "asked IT to install 'the PDF button,' then emailed the committee "
    "a photo of his monitor with the subject line 'bill attached.'"
)


def check_single_sentence(text):
    """One sentence only: a single line ending in one full stop.

    The full stop may sit inside a closing quote, as in ...'bill
    attached.' — so quotes are stripped before the ending is checked.
    """
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    stripped = text.rstrip("'\"")
    if text.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def check_not_blank(text):
    """The gate refuses text that is only whitespace."""
    if not text.strip():
        raise ValueError("entry must not be blank")


def check_within_limit(text):
    """The gate caps the entry at MAX_CHARS characters."""
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )


def resolve_output_path():
    """Entry file: ENTRY_OUT wins, else ENTRY_OUT_DIR/entry.txt."""
    out = os.environ.get("ENTRY_OUT")
    if not out:
        out_dir = os.environ.get("ENTRY_OUT_DIR", "/output")
        out = os.path.join(out_dir, "entry.txt")
    return out


def main():
    """Validate the single sentence and write it to the entry file."""
    text = ROAST.strip()
    check_not_blank(text)
    check_single_sentence(text)
    check_within_limit(text)
    out = resolve_output_path()
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)
    print("(%d characters)" % len(text))


if __name__ == "__main__":
    main()
