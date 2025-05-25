import pandas as pd

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
df = pd.DataFrame({"Name": ["Dev", "Vivek", "Shubham"], "Marks": [100, 90, 90]}, index=['a', 'b', 'c'])

print(s)

print(df)

print()
df = pd.read_csv("CSV/data.csv")

print(df)

print("\n")
print("head", df.head())
print("\n")
print("tail", df.tail())
print("\n")
print("describe", df.describe())
print("\n")
print("\ninfo", df.info())

print("\ndf['ID']\n", df[['ID', 'Age']])
df = df.head(5)
df2 = df.tail(4)
print("\n\n", pd.merge(df, df2))

print("\n\n", pd.concat([df, df2]))
