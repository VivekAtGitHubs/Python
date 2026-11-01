from collections import namedtuple
Employee = namedtuple("Employee", ["name", "dept", "salary"])
emp = Employee("Amit", "IT", 50000)
updated_emp = emp._replace(salary=emp.salary + 5000)
print("Original employee:", emp)
print("Updated employee:", updated_emp)