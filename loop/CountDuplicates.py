items = [1, 2, 3, 2, 4, 1, 2, 5, 4, 4]
dup = []
for i in items:
    count = 0
    for j in items:
        if i == j:
            count = count + 1
    if count > 1 and i not in dup:#element must appear more than once.element must not already be present in the duplicate list.
        dup.append(i)
        print(i, "appears", count, "times")
print("Duplicate elements:", dup)