count = 0
for num in range(2, 51):
    for i in range(2, num):#checks whether num is divisible by any number from 2 to num-1.
        if num % i == 0:
            break
    else:
        print(num, end=" ")#end=" " prints numbers on the same line with spaces.
        count = count + 1
print("\nTotal prime numbers:", count)