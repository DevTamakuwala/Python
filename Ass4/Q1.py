import numpy as np
import pandas as pd

#array_3d = np.linespace(24).reshape(2,3,4)

array_3d = np.arange(10,34).reshape(2,3,4)

print("Original Array:- ")
print(array_3d)

reshaed = array_3d.reshape(3,4,2)
print("\nReshaped Array:-")
print(reshaed)

a1 = np.array([[1,2,3],[4,5,6]])
a2 = np.array([[7,8,9],[10,11,12]])

additions = a1 + a2
sub = a1 - a2 
div = a1 / a2 
mup = a1 * a2

print("--------------------------")
print("additions:\n",additions)
print("--------------------------")
print("Subtraction\n",sub)
print("--------------------------")
print("Divison:\n",div)
print("--------------------------")
print("Multication:\n",mup)

array = np.array([5,6,75,8,19,15])


sqrt_array = np.sqrt(array)
log_array = np.log(array)
exp_array = np.exp(array)

print("--------------------------")
print("Square Root:-\n",sqrt_array)
print("--------------------------")
print("Logarrithm:-\n",log_array)
print("--------------------------")
print("Exponentiation:-\n",exp_array)
print("--------------------------")

data = np.array([25,59,12,14,79])

mean_value = np.mean(data)
median_value = np.median(data)
variance_value = np.var(data)
sta_dev_value = np.std(data)

print("Mean-Value:\n",mean_value)
print("----------------------------")
print("Median-Value\n",median_value)
print("----------------------------")
print("variance-Value,\n",variance_value)
print("----------------------------")
print("Standard_Deviation\n",sta_dev_value)
print("----------------------------")

identiy_matrix = np.eye(3)
square_matixe = np.array([[1,2,3],[4,5,6],[7,8,9]])
dia_elements = np.diag(square_matixe)

print("Identity_Matrix:\n",identiy_matrix)
print("----------------------------")
print("Diagonal_Elements\n",dia_elements)

ver_stacked = np.vstack((a1,a2))
hor_split = np.hsplit(a1,3)

print("Vertically:\n",ver_stacked)
print("----------------------------")
print("Horizontally:\n",hor_split)




