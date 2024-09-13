# Exercise 15:
# Merge two DataFrames on a key.

import pandas as pd

data1 = {'key': ['X', 'Y', 'Z'], 'value1': [1, 2, 3]}
data2 = {'key': ['X', 'Y', 'D'], 'value2': [4, 5, 6]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

merged_df = pd.merge(df1, df2, on='key')
print(merged_df)