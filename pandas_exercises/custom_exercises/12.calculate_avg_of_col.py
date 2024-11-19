"""
Write a Python script to read a CSV file, calculate the average value of a column,
and save the results to a new CSV file.
"""


import pandas as pd

file_location = "C:\\Users\\ertan\\Downloads\\Customer_Contracts.csv"

df = pd.read_csv(file_location)

# print(df.head(5))
# print(df.dtypes)

avg_of_col = df['contract_amount_m'].mean()

print(f"Average amount of a contract: {avg_of_col:.2f}")

# Save into csv
avg_df = pd.DataFrame({'Average Contract Amount': [avg_of_col]})
avg_df.to_csv("average_contract_amount.csv", index=False)

