book = {
    "Rahul": 9876543210,
    "Vivek": 9876543211,
    "Aman": 9876543212
}
name = input("Enter a name: ")
number = book.get(name, "Not found")
print(number)