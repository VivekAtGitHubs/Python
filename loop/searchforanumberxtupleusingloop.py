nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 49
idx = 0
#For each element in the list, check whether the current element is equal to x
for el in nums:
    if el == x:
        print("number found at idx", idx)
        break
    idx =idx+ 1