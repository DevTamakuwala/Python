import pandas as pd
import numpy as np

# Load dataset (Replace 'your_file.csv' with actual file path)

df = pd.read_csv("E:\MCA_SCI\sem2\PY\CSV\employee_data.csv")  # Use full path

# (a) Display first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# (b) Summary statistics: mean, median, std for numerical columns
print("\nSummary Statistics:")
print(df.describe())

print("\nMedian values:")
print(df.median(numeric_only=True))

print("\nStandard Deviation:")
print(df.std(numeric_only=True))

# (c) Count the number of unique values in each column
print("\nUnique values count per column:")
print(df.nunique())

# (d) Find the most frequent value in each column
print("\nMost frequent values in each column:")
print(df.mode().iloc[0])  # Takes the first mode value if multiple exist
