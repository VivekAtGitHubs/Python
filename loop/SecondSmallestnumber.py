nums = [23,67,12,89,45,8,20]
smallest = nums[0]
second_smallest= nums[0]
for n in nums :
    # if the current number is smaller than the smallest number, move the previous smallest number to second-smallest and update the smallest with the current number
    if n < smallest:
         second_smallest =smallest
         smallest = n    
# If the current number is greater than the smallest number but smaller than the current second-smallest number
    elif n < second_smallest and n!= smallest:
         Second_smallest = n
print("Smallest",smallest)
print("Second_smallest",second_smallest)         