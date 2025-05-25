import pandas as pd
import numpy as np

# Load voter data from the CSV file
df_voters = pd.read_csv(r"E:\MCA_SCI\sem2\PY\CSV\voter_data.csv")

# Check voting eligibility (age >= 18)
df_voters['Eligible_to_vote'] = df_voters['Voter_age'].apply(
    lambda age: 'Yes' if pd.notna(age) and age >= 18 else ('Not Sure' if pd.isna(age) else 'No')
)

# Save the result to a new CSV file
df_voters.to_csv('voter_data_with_eligibility.csv', index=False)

# Display the updated DataFrame
print(df_voters)
