students = {
    1: {"name": "Rahul", "gpa": 8.2},
    2: {"name": "Vivek", "gpa": 9.1},
    3: {"name": "Aman", "gpa": 8.7}
}
# Print all student details
for student_id, details in students.items():
    print("Name:", details["name"])
    print("GPA:", details["gpa"])
# Find student with highest GPA
highest_gpa = 0
best_student = ""
for student_id, details in students.items():
    if details["gpa"] > highest_gpa:
        highest_gpa = details["gpa"]
        best_student = details["name"]
print("Highest GPA student:", best_student)
print("Highest GPA:", highest_gpa)