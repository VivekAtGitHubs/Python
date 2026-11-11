#5Fibbonacci series sequence in which each number is sum of previous btwo numbers
# 5





n=int(input("enter the number"))
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c