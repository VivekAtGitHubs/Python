#Correct way: create a separate copy
original = [1, 2, 3]
backup = original.copy()
backup.append(99)
print("Original:", original)
print("Backup:", backup)
# original did NOT change because .copy() creates
# a separate list object.
# Deliberately create the bug using =
original = [1, 2, 3]
backup = original
backup.append(99)
print("Original after using = :", original)
print("Backup after using = :", backup)
# Both lists changed because backup and original
# refer to the SAME list object.
