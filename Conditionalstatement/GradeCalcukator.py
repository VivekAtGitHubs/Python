marks = int(input("enter the marks"))
if marks<0 and marks>100 :
    print("invalid marks",marks)
elif marks>=90 :
    print("A++ oustanding")
elif marks>=75:
    print("A",marks)
elif marks>=60 :
    print("B",marks)
elif marks>=33:
    print("C",marks)
else:
    print("fail",marks)
