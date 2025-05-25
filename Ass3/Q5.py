import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv(r"E:\MCA_SCI\sem2\PY\weather_data.csv")

# (i) Compute the sum of every column
print("Sum of each column:")
print(df.sum(numeric_only=True))  # numeric_only=True ensures only numerical columns are summed

# (ii) Compute the mean of the "RainFall" column
rainfall_mean = df["RainFall"].mean()
print("\nMean of RainFall column:", rainfall_mean)

# (iii) Compute the median of the "MaxTemp" column
maxtemp_median = df["MaxTemp"].median()
print("\nMedian of MaxTemp column:", maxtemp_median)

# (iv) Display all column names
print("\nColumn names:")
print(df.columns.tolist())
