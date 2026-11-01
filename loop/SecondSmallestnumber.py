nums = [23,67,12,89,45,20]
smallest = nums[0]
second_smallest= nums[0]
for n in nums :
    if n < smallest:
        smallest = n
    elif n > second_smallest and n!= smallest:
        Second_smallest = n
print("Smallest",smallest)
print("Second_smallest",second_smallest)         