text = input("enter the string")
rev =""
for ch in text :
    rev = ch +  rev
if text == rev :
  print("pallindrome number")
else:
    print("not pallindrome")           