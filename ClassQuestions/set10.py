import pandas as pd

data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,111,112],
    'Name': ['Alice','jenil', 'Bob', 'Charlie', 'David', 'Eva','jenil', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    'Age': [25, None, 30, 28, 56,35, None, 40, 27, 23, None,56],
    'Percentage': [85.4, 78.0, None, 92.5, 88.0, 74.5, None, 81.2, 79.6, None,80.3,94.2]
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df)
print("\nMissing values in 'Age' and 'Percentage' columns:\n", df[['Age', 'Percentage']].isnull().sum())

#blank space replaced with mean
df.fillna({'Age': df['Age'].mean(), 'Percentage': df['Percentage'].mean()}, inplace=True)
print("\nDataset after replacing missing values with mean:\n", df)

#alternate method==>median
df.fillna({'Age': df['Age'].median(), 'Percentage': df['Percentage'].median()}, inplace=True)
print("\nDataset after replacing missing values with median:\n", df)

df = pd.DataFrame(data)

## Check for duplicates based on Name and Age
duplicates = df[df.duplicated(subset=['Name', 'Age'])]

# Remove duplicates based on Name and Age
df_cleaned = df.drop_duplicates(subset=['Name', 'Age'])

print("Duplicate Records:\n", duplicates)
print("\nCleaned DataFrame:\n", df_cleaned)

