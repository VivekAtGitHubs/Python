def cal_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i  # corrected from 1 to i
    print(fact)

cal_fact(6)  # corrected function name
