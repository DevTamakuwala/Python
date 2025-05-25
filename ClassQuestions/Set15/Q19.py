import pandas as pd

data = {
    'Product': ['Laptop', 'Tablet', 'Smartphone', 'Printer'],
    'Price': [85000, 30000, 45000, 15000],
    'Quantity': [10, 25, 15, 12]
}

df = pd.DataFrame(data)
df['Total_Value'] = df['Price'] * df['Quantity']
print("With Total_Value:\n", df)

filtered = df[df['Total_Value'] > 500000]
print("\nFiltered Products (Total Value > ₹5,00,000):\n", filtered)

sorted_df = df.sort_values(by='Total_Value', ascending=False)
print("\nSorted by Total_Value:\n", sorted_df)
