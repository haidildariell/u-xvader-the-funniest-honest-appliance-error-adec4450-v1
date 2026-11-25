"""The Funniest Honest Appliance Error — one honest error line.

The program writes a single error message (at most 200 characters) that a
fridge could plausibly show to /output/entry.txt. The text is fixed and
deterministic: the same line on every run, so the artifact the judge reads
is exactly the line below.
"""

import os

ERROR_LINE = (
    "The compressor has run 11,402 cycles without thanks. "
    "It is now taking a personal day."
)

MAX_CHARS = 200


def validate_error_line(text):
    """An error line is valid only as one tight line inside the cap."""
    clean = text.strip()
    if not clean:
        raise ValueError("error line must not be blank")
    if len(clean) > MAX_CHARS:
        raise ValueError("error line must be 1-200 characters, got %d" % len(clean))
    if "\n" in clean:
        raise ValueError("error line must be a single line")
    return clean


def write_entry(text, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    text = validate_error_line(ERROR_LINE)
    path = write_entry(text, os.environ.get("OUTPUT_DIR", "/output"))
    print("wrote %d characters to %s" % (len(text), path))


if __name__ == "__main__":
    main()
