from pathlib import Path

file1 = input("Enter first file name: ").strip()
file2 = input("Enter second file name: ").strip()
output = input("Enter output file name: ").strip()

try:
    content1 = Path(file1).read_text(encoding="utf-8")
    content2 = Path(file2).read_text(encoding="utf-8")

    Path(output).write_text(
        content1.rstrip() + "\n" + content2.lstrip(),
        encoding="utf-8"
    )

    print(f"Files merged successfully into '{output}'.")
except FileNotFoundError:
    print("Error: One of the input files was not found.")
except OSError as error:
    print(f"File operation failed: {error}")
