nums = [23, 67,76, 12, 89, 45]
largest = nums[0]
second_largest = nums[0]
for n in nums:
#"If you find a new largest number, move the previous largest number into second-largest,and make the current number the new largest number    
    if n > largest:
        second_largest = largest
        largest = n
#If the current number is smaller than the largest number but greater than the second-largest number, then make it the new second-largest number
    elif n>second_largest  and n!=largest :
        second_largest = n
print("Largest:", largest)
print("Second Largest:", second_largest)