# Practice 1: Count Total Lines in a File

from pathlib import Path

filename = input("Enter file name: ").strip()

try:
    lines = Path(filename).read_text(encoding="utf-8").splitlines()
    print(f"Total lines: {len(lines)}")
except FileNotFoundError:
    print("Error: File not found.")
except OSError as error:
    print(f"Error reading file: {error}")
