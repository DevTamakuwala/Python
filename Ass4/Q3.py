import numpy as np

data = np.loadtxt(r"E:\MCA_SCI\sem2\PY\CSV\sample_data.csv", delimiter=',', skiprows=1)


column_index = 1  # change this index based on your need

column_data = data[:, column_index]
column_sum = np.sum(column_data)
column_avg = np.mean(column_data)

print(f"Sum of column {column_index}: {column_sum}")
print(f"Average of column {column_index}: {column_avg}")
