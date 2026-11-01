age = int(input("enter the age"))
citizen_score = int(input("enter the citizen_score"))
national_score = int(input("enter the national_score"))
if age>=18 :
    if citizen_score>=40:
        if national_score>=60:
            print("you are eligible to vote")
        else:
            print(" not eligible to vote,improve your national score")
    else:
        print("not eligible to vote,impove your citizen score" )
else:
   print("not eligible to vote,age should be  equal to or greater than 18")