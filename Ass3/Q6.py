import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv(r"E:\MCA_SCI\sem2\PY\data.csv")

# Display the first 10 rows
print("First 10 Rows:")
print(df.head(10))

# Display the list of all column names
print("\nList of all Columns:")
print(df.columns.tolist())
