my_tuple = (
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    )

#Create a tuple containing three lists. 
#Each list should contain three integers. Access the second element of the second list.

second_element = my_tuple[1][1]

print(second_element)

#Modify a list that is inside a tuple.
#Create a tuple containing a list of integers, modify one of the integers in the
#list, and print the updated tuple.
my_tuple[0][1] = 6

print(my_tuple)

#3Write a function that takes a tuple of
#lists as input. The function should return a list of the sums of each inner
#list in the tuple.
    
def sum_of_inner_lists(tuple_of_lists):
    return [sum(lst) for lst in my_tuple]

print(sum_of_inner_lists(my_tuple))

# 4. Create a tuple containing a list of
# strings. Update the string at the second position in the list and print the
# updated tuple.

tuple_with_strings = (["apple", "banana", "cherry"],)

tuple_with_strings[0][1] = "green apple"

print(tuple_with_strings) 

#5. Function to remove the first element from each list inside a tuple.

def remove_first_element(tuple_of_lists):
    return tuple(lst[1:] for lst in tuple_of_lists)

print(remove_first_element(my_tuple))  

#6. Create a tuple with a nested list, add an element, and append the tuple to another list.

nested_tuple = ([10, 20, 30],)

nested_tuple[0].append(40)

outer_list = []
outer_list.append(nested_tuple)

print(outer_list)  

#7. Function to return a new tuple where each list inside is sorted in ascending order.

def sort_inner_lists(tuple_of_lists):
    return tuple(sorted(lst) for lst in tuple_of_lists)

ex_tuple = ([3, 1, 2], [6, 4, 5], [9, 8, 7])

print(sort_inner_lists(ex_tuple))  

#8. Create a tuple with a list of tuples, sum all numbers, and return the result.

def sum_inner_tuples(tuple_of_tuples):
    return sum(sum(tpl) for tpl in tuple_of_tuples)

example_tuple = ((1, 2), (3, 4), (5, 6))

print(sum_inner_tuples(example_tuple))  
