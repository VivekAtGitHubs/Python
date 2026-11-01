for i in range(5):
    for j in range(5):
        if i == 1 and j == 2:
            continue
        print("*", end=" ")
    print()