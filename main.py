"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings to
<output>/entry.txt. Deterministic, stdlib-only, no network, no randomness.
"""

import os

LABEL = "WARNING: This human says 'I'm five minutes away' and has not left the house."

MAX_CHARS = 160


def resolve_output_dir():
    """The grader sets MAKEFUN_OUTPUT_DIR; default to /output per the rules."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate_entry(text):
    """Check the label against the RULES.txt gate before it is accepted.

    A valid entry is one line, 1-160 chars, and not blank. The check runs
    on the text read back from disk, so what is verified is exactly what
    the grader will read.
    """
    assert 1 <= len(text) <= MAX_CHARS, "entry length %d outside 1-160" % len(text)
    assert text.strip(), "entry is blank"
    assert "\n" not in text, "entry must be a single line"
    return text


def write_label(path):
    """Write LABEL to path, read it back, and validate the round trip."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(LABEL)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return validate_entry(text)


def main():
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = write_label(path)
    print("Wrote %d chars to %s" % (len(text), path))


if __name__ == "__main__":
    main()
