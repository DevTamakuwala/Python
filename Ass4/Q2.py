import numpy as np

np.random.seed(42)
array6 = np.random.uniform(15, 35, 7)


print("\nTemperature value: \n", array6)

print("\nMaximum temp: \n", np.max(array6))

print("\nMinimum temp: \n", np.min(array6))

print("\nAverage temp: \n", np.average(array6))