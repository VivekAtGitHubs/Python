name = input("Enter a string: ")
rev = ""
i = len(name) - 1
while i >= 0:
    rev = rev + name[i]
    i = i - 1
print("Reversed string:", rev)