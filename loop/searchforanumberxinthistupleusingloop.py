nums  = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
#While the index i is less than the length of the list, check whether the element at index i is equal to x
while i < len(nums):
    if nums[i] == x:
        print("Found at idx", i)
    else:
        print("finding")
    i = i +1
