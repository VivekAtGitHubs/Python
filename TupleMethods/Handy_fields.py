from collections import namedtuple
Student = namedtuple("Student", ["name", "age", "course", "gpa"])
s = Student("Amit", 21, "BCA", 8.5)
print(Student._fields)