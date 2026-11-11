text = input("Enter a string: ")
rev = ""
i = len(text) - 1
while i >= 0:
    rev = rev + text[i]
    i = i - 1
if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")