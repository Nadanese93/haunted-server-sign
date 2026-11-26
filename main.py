"""Write the one-liner entry to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os
import sys

ENTRY = "PING 666ms — the ghost answers. Packet loss means it is standing right behind you."


def verify(out_dir: str) -> None:
    """Read entry.txt back and validate it against ENTRY; exit 1 on any failure."""
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "rb") as f:
        raw = f.read()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        print("verify failed: entry.txt is not valid UTF-8", file=sys.stderr)
        sys.exit(1)
    if not 1 <= len(text) <= 120:
        print(f"verify failed: entry is {len(text)} chars, must be 1-120", file=sys.stderr)
        sys.exit(1)
    if text.endswith("\n"):
        print("verify failed: entry.txt has a trailing newline", file=sys.stderr)
        sys.exit(1)
    if raw != ENTRY.encode("utf-8"):
        print("verify failed: entry.txt is not byte-identical to ENTRY", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(ENTRY.encode("utf-8"))
    verify(out_dir)


if __name__ == "__main__":
    main()
