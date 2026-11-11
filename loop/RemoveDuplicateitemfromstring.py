text = input("enter a String")
unique = ""
for ch in text:
    if ch not in unique :
        unique=unique+ch
print("String without Duplicates",unique)        
