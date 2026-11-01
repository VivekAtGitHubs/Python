from collections import namedtuple
Student = namedtuple("Student", ["name", "age", "course", "gpa"])
s = Student("Amit", 21, "BCA", 8.5)
#_replace change a field (make a new record)
s2 = s._replace(gpa=9.0)
print(s.gpa)
print(s2)