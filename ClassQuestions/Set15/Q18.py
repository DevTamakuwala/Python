import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 78, 90],
    'Science': [92, 81, 95],
    'English': [88, 74, 85]
}

df = pd.DataFrame(data)
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)
print("DataFrame with Average:\n", df)

# Filter
high_scorers = df[(df['Math'] > 85) & (df['Science'] > 85) & (df['English'] > 85)]
print("\nStudents scoring above 85 in all subjects:\n", high_scorers)
