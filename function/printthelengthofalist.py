cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list_to_print):
    print("Length of list:", len(list_to_print))
    print_list(list_to_print)

def print_list(list_to_print):
    for item in list_to_print:
        print(item, end=" ")
    print()  # for newline

print_len(cities)
print_len(heroes)
