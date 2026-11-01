from collections import namedtuple
Employee = namedtuple("Employee", ["name", "dept", "salary"])
emp = Employee("Amit", "IT", 50000)
d = emp._asdict()
print(d)