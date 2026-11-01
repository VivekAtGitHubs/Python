
from collections import namedtuple

student = namedtuple("student", ["name", "age", "course", "gpa"])

s = student("amit", 21, "bca", 8.5)

print(s.name)
print(s.gpa)
print(s[0])
point = namedtuple("point","x y")
p = point(10,20)
print(p.x,p.y)