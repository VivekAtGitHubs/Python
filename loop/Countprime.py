count = 0
for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count = count + 1
print("\nTotal prime numbers:", count)