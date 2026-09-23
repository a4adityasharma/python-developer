# Practice 5: Create and Read a JSON File

import json

data = {
    "name": "Aditya",
    "course": "Python Programming",
    "week": 3,
    "skills": ["OOP", "Exception Handling", "Python Libraries"]
}

filename = "practice_data.json"

try:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"JSON file '{filename}' created successfully.")

    with open(filename, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)

    print("\nData read from JSON:")
    print(json.dumps(loaded_data, indent=4))

except OSError as error:
    print(f"File operation failed: {error}")
except json.JSONDecodeError:
    print("Invalid JSON data.")
