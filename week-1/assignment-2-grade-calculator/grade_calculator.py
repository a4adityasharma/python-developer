num_subjects = int(input("Enter the number of subjects: "))

marks = []
total = 0

for i in range(1, num_subjects + 1):
    mark = float(input(f"Enter marks for subject {i}: "))
    while mark < 0 or mark > 100:
        print("Marks should be between 0 and 100.")
        mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)
    total += mark

average = total / num_subjects

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"\nAverage marks: {average:.2f}")
print(f"Grade: {grade}")