# Q1. Create a Pandas DataFrame using a two-dimensional list. Perform the following operations:-
# Count the number of rows
# Count missing values in the first column
# Display the number of columns in the DataFrame
# Use statistical techniques to fill missing values and draw different charts showing dataset clustering

import pandas as pd
import numpy as np

# Creating a Pandas DataFrame using a 2D list
data = [
    [1, 'Alice', 25, np.nan],
    [2, 'Bob', np.nan, 45000],
    [3, 'Charlie', 30, 50000],
    [4, 'David', 35, np.nan],
    [5, 'Eve', np.nan, 60000]
]

columns = ['ID', 'Name', 'Age', 'Salary']
df = pd.DataFrame(data, columns=columns)

# (a) Count the number of rows
num_rows = df.shape[0]
print("Number of rows:", num_rows)

# (b) Count missing values in the first column
missing_values_first_col = df.iloc[:, 0].isnull().sum()
print("Missing values in first column:", missing_values_first_col)

# (c) Display the number of columns in the DataFrame
num_columns = df.shape[1]
print("Number of columns:", num_columns)

# (d) Fill missing values using mean for 'Age' and median for 'Salary'
df.fillna({'Age': df['Age'].mean(), 'Salary': df['Salary'].median()}, inplace=True)

print("\nDataFrame after filling missing values:")
print(df)
