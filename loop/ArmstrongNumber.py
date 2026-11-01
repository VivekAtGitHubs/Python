#Armstrong Number equal to sum of its digits where each is raised to power of total number of digits
num = int(input("Enter a number: "))
temp = num
digits = len(str(num))
total = 0
while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10
if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
