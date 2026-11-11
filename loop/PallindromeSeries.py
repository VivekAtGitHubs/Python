for num in range(1, 101):
    temp = num # creating copies
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    if num == rev:
        print(num, end=" ")