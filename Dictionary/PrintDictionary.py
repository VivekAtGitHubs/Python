#Dictionary store key  value pair and uses hashing 
# to find any value instantly
#key must be hashable(immutable) string ,
d1 = {
    "name": "Rajeev",
    "age": 16,
    "marks": [23, 29, 30],
    "isgood": True
}
print(d1["name"])
print(d1["marks"])
print(type(d1))