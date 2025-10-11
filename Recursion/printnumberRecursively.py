def show(n):
    if n == 0:   # base case
        return
    print(n)
    show(n - 1)  # recursive call

# function call
show(10)
