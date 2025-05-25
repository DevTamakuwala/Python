import numpy as np

original_array = np.array([10, 20, 30])
values_to_append = [40, 50, 60, 70, 80, 90]

new_array = np.append(original_array, values_to_append)

print("Original array:", original_array)
print("After append values to the end of the array:", new_array)
