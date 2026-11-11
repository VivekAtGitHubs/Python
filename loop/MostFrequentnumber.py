items = [3,1,3,2,3,1,2,3]
most_frequent =items[0]
highest_count = 0
for i in items :# select each element one by one 
    count = 0
    for j in items :#comapre each element in the list
        if i==j :
            count=count+1 #if both equal then increase with one 
            if count>highest_count :
                most_frequent = i
print("Most frequent",most_frequent)
print("Count",highest_count)