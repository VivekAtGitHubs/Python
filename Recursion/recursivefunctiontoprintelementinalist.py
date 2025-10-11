def print_list_elements(lst, index=0):
    if index == len(lst):
        return
    print(lst[index])
    print_list_elements(lst, index + 1)

# Example usage:
my_list = [10, 20, 30, 40, 50]
print_list_elements(my_list)
