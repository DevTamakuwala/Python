import pandas as pd

# Read the CSV file
df = pd.read_csv(r"E:\MCA_SCI\sem2\PY\CSV\products.csv")

# Compute total price of all products
total_price = df["Price"].sum()
print("Total Price of all products:", total_price)

# Compute the maximum profit from given products
max_profit = df["Profit"].max()
print("Maximum Profit from given products:", max_profit)
