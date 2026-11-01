nums = [34, 12, 78, 5, 60]
smallest = nums[0]
for i in nums:
    if i < smallest:
        smallest = i
print("Smallest number:", smallest)
