num =int(input("enter the number"))
rev=0
for i in range (len(str(num))):
     digit =num%10
     rev= rev*10+digit
     num=num//10
print("reverse of a number",rev)