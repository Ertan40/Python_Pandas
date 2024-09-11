# Exercise 4:
# Filter rows based on a column condition

import pandas as pd

data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}

df = pd.DataFrame(data)
filtered_df = df[df['X'] > 2]

print(filtered_df)