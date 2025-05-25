# 4. Write a function remove_duplicates(lst) that removes duplicate values from a list and returns
# the list with only unique elements, preserving the original order.

def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage:
lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("List after removing duplicates:", remove_duplicates(lst))
