from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 7)
print("X coordinate:", p.x)
print("Y coordinate:", p.y)