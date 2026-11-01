from collections import namedtuple
#define shape a name+itsfields
student = namedtuple("student", ["name", "age", "course", "gpa"])
s = student("amit", 21, "bca", 8.5)
print(s.name)
print(s.gpa)
print(s[0])