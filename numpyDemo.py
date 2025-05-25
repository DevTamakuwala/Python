import numpy as np

arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
arr2 = np.linspace(0, 15, 16)
arr3 = np.arange(0, 15)
arr4 = np.zeros(20, int)
arr5 = np.ones(20, int)

print(arr2d)
print()
print(arr1d)
print()
print(arr2)
print()
print(arr3)
print()
print(arr4)
print()
print(arr5)

arr1d2 = arr1d + 5
arr1d3 = arr1d + arr1d2
# shellow copy
arr1d22 = arr1d2.view()
# deep copy
# arr1d22 = arr1d2.copy()


print()
print(arr1d)
print(arr1d2)
print()
print(arr1d3)
print()
print(arr1d22)
