my_tuple = (
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    )
print("Tuple With Frist Element:-")
print(my_tuple)

def remove_first_element(tuple_of_lists):
    return tuple(lst[1:] for lst in my_tuple)

print("Tuple Without Frist Element:-")
print(remove_first_element(my_tuple)) 