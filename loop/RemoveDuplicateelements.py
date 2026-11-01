items =[1,2,2,3,4,4,4,5]
unique = []
for n in items :
    if n not in unique:
        unique.append(n)
print(unique)