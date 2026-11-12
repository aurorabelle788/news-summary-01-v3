"""news-summary-01 entry v3 (Python 3.13, standard library only).

The summary text lives in summary.txt next to this file. The program
copies it byte for byte to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output). No network, no clock, no randomness, so both runs write the
same bytes. The gate allows 1 to 2,000 characters (Unicode code points),
so the text is checked against those bounds before writing, and the
written file is read back and compared to the source. The summary is a
fixed text: the entry does not fetch, generate, or alter it.
"""

import os
from pathlib import Path

BASE = Path(__file__).resolve().parent
DEST = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def run() -> None:
    source = BASE / "summary.txt"
    data = source.read_bytes()
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 2000:
        raise ValueError(f"summary is {len(text)} characters, gate allows 1-2000")
    if not text.strip():
        raise ValueError("summary is only white space")
    DEST.mkdir(parents=True, exist_ok=True)
    out = DEST / "entry.txt"
    out.write_bytes(data)
    if out.read_bytes() != data:
        raise ValueError("written entry does not match the summary")


if __name__ == "__main__":
    run()
