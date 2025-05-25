import pandas as pd

# Create a DataFrame with marks of 4 students
data = {
    'Student': ['Jenil', 'Sajjad', 'Akshay', 'Dev'],
    'Math': [88, 92, 95, 70],
    'Science': [90, 85, 91, 88],
    'English': [85, 89, 86, 90]
}

df = pd.DataFrame(data)

# Add a column for Highest Mark
df['Highest Mark'] = df[['Math', 'Science', 'English']].max(axis=1)

# Rank based on Highest Mark (higher marks = higher rank)
df['Rank'] = df['Highest Mark'].rank(ascending=False).astype(int)

# Sort by Rank
df = df.sort_values(by='Rank')

print(df)
