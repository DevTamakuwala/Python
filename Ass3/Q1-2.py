import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Creating a DataFrame using a two-dimensional list with some missing values
data = [
    [1, "A", 20, np.nan],
    [2, "B", 25, 15.5],
    [3, "C", 22, 18.3],
    [4, np.nan, 27, 20.1],
    [5, "E", np.nan, 16.4],
    [6, "F", 23, np.nan]
]

# Defining column names
columns = ["ID", "Category", "Age", "Score"]

# Creating DataFrame
df = pd.DataFrame(data, columns=columns)

# a. Count number of rows
num_rows = len(df)
print("Number of rows:", num_rows)

# b. Count missing values in the first column
missing_values_col1 = df["Category"].isnull().sum()
print("Number of missing values in the first column:", missing_values_col1)

# c. Display number of columns in the DataFrame
num_columns = df.shape[1]
print("Number of columns in the DataFrame:", num_columns)

# d. Filling missing values using mean for numerical columns
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Score"].fillna(df["Score"].mean(), inplace=True)

# Filling missing values in categorical column using mode
df["Category"].fillna(df["Category"].mode()[0], inplace=True)

print("\nDataFrame after filling missing values:")
print(df)

# Plotting charts for clustering of datasets
plt.figure(figsize=(10, 5))

# Scatter plot showing Age vs Score
plt.subplot(1, 2, 1)
sns.scatterplot(x=df["Age"], y=df["Score"], hue=df["Category"], palette="viridis")
plt.title("Age vs Score Clustering")

# Bar plot for categorical distribution
plt.subplot(1, 2, 2)
sns.countplot(x=df["Category"], palette="coolwarm")
plt.title("Category Distribution")

plt.show()
