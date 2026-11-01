nums = [23, 67, 12, 89, 45]
largest = nums[0]
second_largest = nums[0]
for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n
print("Largest:", largest)
print("Second Largest:", second_largest)