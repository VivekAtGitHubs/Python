d1 = {
    "name":"Vivek",
    "Education":"btech",
    "age":16,
    "marks":[23,24,21],
     2:"hello"
}
# Create add item in Dictionary -d1["what to add" ]
d1["average"] = 22.4
print(d1)
# update - update the name d1["what to update"]
d1["name"] = "Vivek Yadav"
# del d1[what to remove] Delete the items
del d1[2]
print(d1)
#d1.pop("remove the item")
del_value =d1.pop("marks")
print(del_value)
print(d1)