students = [
    {"name": "Aman", "marks": 78},
    {"name": "Riya", "marks": 92},
    {"name": "Karan", "marks": 85},
    {"name": "Neha", "marks": 69},
]

students.sort(key=lambda student: student["marks"])

print("Students sorted by marks:")
for student in students:
    print(f'{student["name"]}: {student["marks"]}')
