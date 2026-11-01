from collections import namedtuple
Student = namedtuple("Student", ["name", "age", "gpa"])
rows = [
    ["Amit", 21, 8.5],
    ["Neha", 20, 9.1],
    ["Ravi", 22, 7.8]
]
for row in rows:
    student = Student._make(row)
    print("Name:", student.name, "| GPA:", student.gpa)