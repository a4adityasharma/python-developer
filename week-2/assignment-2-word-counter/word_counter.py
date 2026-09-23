from pathlib import Path


def count_file_content(filename):
    try:
        file_path = Path(filename)

        with file_path.open("r", encoding="utf-8") as file:
            content = file.read()

        words = content.split()
        lines = content.splitlines()
        characters = len(content)

        return len(words), len(lines), characters

    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")
        return None

    except OSError as error:
        print(f"Error reading file: {error}")
        return None


def main():
    filename = input("Enter text file name: ").strip()

    result = count_file_content(filename)

    if result is not None:
        words, lines, characters = result

        print("\nFile Statistics")
        print("-" * 30)
        print(f"Words      : {words}")
        print(f"Lines      : {lines}")
        print(f"Characters : {characters}")


if __name__ == "__main__":
    main()
