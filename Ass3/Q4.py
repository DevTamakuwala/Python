import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv(r"E:\MCA_SCI\sem2\PY\employee_data.csv")
# Replace with your actual file name

# (i) Fill all 'NaN' values with the mean of the respective column
df.fillna(df.mean(numeric_only=True), inplace=True)

# (ii) Display the last 5 rows
print("Last 5 rows of the DataFrame:")
print(df.tail())

# Save the modified DataFrame (optional)
df.to_csv("updated_employee_data.csv", index=False)
