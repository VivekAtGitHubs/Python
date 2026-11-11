#Fibonacci series is a sequence of numbers in which each new number is the sum of the previous two numbers.
n = int(input("Enter the number of terms: "))
a = 0
b = 1
i = 0
while i < n:# loop will run until i is smaller than n
    print(a)
    c = a + b
    a = b
    b = c
    i =i+ 1