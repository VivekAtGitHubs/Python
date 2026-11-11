items =[1,2,2,3,4,4,4,5]
unique = []
for n in items :
#If the number n is not already present in the unique list, then add it to the list    
    if n not in unique:
        unique.append(n)
print(unique)