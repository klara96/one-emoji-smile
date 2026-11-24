#!/usr/bin/env python3
"""Write the make.fun competition entry text to /output/entry.txt.

The entry is a single hatching chick emoji, which is the most likely emoji to
make a stranger smile.
"""
import os
import sys

def main() -> None:
    output_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)

    entry_text = "<<<🐣>>>\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(entry_text)

if __name__ == "__main__":
    main()
