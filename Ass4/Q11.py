import pandas as pd

# Load event data from the CSV file
df_events = pd.read_csv(r"E:\MCA_SCI\sem2\PY\CSV\event_data.csv")

# Apply discount (e.g., 10%)
df_events['Discounted_Price'] = df_events['Cost'] * 0.90

# Save the result to a new CSV file
df_events.to_csv('event_data_with_discount.csv', index=False)

# Display the updated DataFrame
print(df_events)
