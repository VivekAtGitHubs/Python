student = {
    "name": "Vivek",
    "age": 22,
    "course": "MCA"
}
rev = {}
for key, value in reversed(list(student.items())):
    rev[key] = value
print(rev)