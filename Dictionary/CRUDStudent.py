student = {
    "name": "Rahul",
    "age": 22
}
# 1. Add a course
student["course"] = "MCA"
print("After adding course:", student)
# 2. Update age
student["age"] = 23
print("After updating age:", student)
# 3. Safely read missing email
email = student.get("email", "Email not found")
print("Email:", email)
# 4. Delete course
del student["course"]
print("After deleting course:", student)