#5Fibbonacci series sequence in which each number is sum of previous btwo numbers
n=int(input("enter  number of terms"))
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c