import json


def load_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")

    except json.JSONDecodeError:
        print("Error: The JSON file contains invalid JSON data.")

    except OSError as error:
        print(f"Error reading file: {error}")

    return None


def display_data(data):
    print("\nFormatted JSON Data")
    print("-" * 30)

    if isinstance(data, list):
        for index, item in enumerate(data, start=1):
            print(f"\nRecord {index}:")
            for key, value in item.items():
                print(f"{key.title()}: {value}")

    elif isinstance(data, dict):
        for key, value in data.items():
            print(f"{key.title()}: {value}")

    else:
        print(data)


def main():
    filename = input("Enter JSON file name: ").strip()

    data = load_json(filename)

    if data is not None:
        display_data(data)


if __name__ == "__main__":
    main()
