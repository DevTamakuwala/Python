import numpy as np

array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([10, 30, 40])

common_values = np.intersect1d(array1, array2)

print("Array1:", array1)
print("Array2:", array2)
print("Common values between two arrays:", common_values)

# For 1D array
array_1d = np.array([10, 10, 20, 20, 30, 30])
unique_1d = np.unique(array_1d)
print("Original array:", array_1d)
print("Unique elements of the above array:", unique_1d)

# For 2D array
array_2d = np.array([[1, 1], [2, 3]])
unique_2d = np.unique(array_2d)
print("\nOriginal array:\n", array_2d)
print("Unique elements of the above array:", unique_2d)
