# Exercise 23:
# Filter rows by multiple conditions.

import pandas as pd
data = {'X': [1, 2, 3, 4], 'Y': [4, 5, 6, 7]}

df = pd.DataFrame(data)

filtered_df = df[(df['X'] > 2) & (df['Y'] < 7)]
print(filtered_df)