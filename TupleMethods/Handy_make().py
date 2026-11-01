#Build from a list
from collections import namedtuple
Student = namedtuple("Student", ["name", "age", "course", "gpa"])
row = ["Neha", 20, "BCA", 9.1]
#make()-build frooom a list
s = Student._make(row)
print(s.name, s.gpa,s.course)