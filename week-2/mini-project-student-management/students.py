import csv
from pathlib import Path

FILE_NAME = "students.csv"
FIELDS = ["roll_number", "name", "marks"]


def initialize_file():
    """Create the CSV file with headers if it does not exist."""
    file_path = Path(FILE_NAME)

    if not file_path.exists():
        with file_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


def load_students():
    """Load all student records from the CSV file."""
    initialize_file()

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except OSError as error:
        print(f"Error reading student file: {error}")
        return []


def save_students(students):
    """Save all student records to the CSV file."""
    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(students)
        return True
    except OSError as error:
        print(f"Error saving student data: {error}")
        return False


def add_student():
    students = load_students()

    roll_number = input("Enter roll number: ").strip()

    if not roll_number:
        print("Roll number cannot be empty.")
        return

    if any(student["roll_number"] == roll_number for student in students):
        print("A student with this roll number already exists.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    marks_input = input("Enter marks (0-100): ").strip()

    try:
        marks = float(marks_input)
    except ValueError:
        print("Marks must be a number.")
        return

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    students.append(
        {
            "roll_number": roll_number,
            "name": name,
            "marks": f"{marks:g}",
        }
    )

    if save_students(students):
        print("Student added successfully.")


def search_student():
    students = load_students()

    roll_number = input("Enter roll number to search: ").strip()

    for student in students:
        if student["roll_number"] == roll_number:
            print("\nStudent Found")
            print("-" * 30)
            print(f"Roll Number: {student['roll_number']}")
            print(f"Name       : {student['name']}")
            print(f"Marks      : {student['marks']}")
            return

    print("Student not found.")


def delete_student():
    students = load_students()

    roll_number = input("Enter roll number to delete: ").strip()

    updated_students = [
        student
        for student in students
        if student["roll_number"] != roll_number
    ]

    if len(updated_students) == len(students):
        print("Student not found.")
        return

    if save_students(updated_students):
        print("Student deleted successfully.")


def display_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 60)
    print(f"{'Roll No.':<12}{'Name':<25}{'Marks':<10}")
    print("-" * 60)

    for student in students:
        print(
            f"{student['roll_number']:<12}"
            f"{student['name']:<25}"
            f"{student['marks']:<10}"
        )


def main():
    initialize_file()

    while True:
        print("\n" + "=" * 40)
        print("      STUDENT MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Display Students")
        print("5. Exit")
        print("=" * 40)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Exiting Student Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
