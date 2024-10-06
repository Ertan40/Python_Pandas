# Exercise 40:
# Filter rows based on datetime index.

import pandas as pd

date_range = pd.date_range(start='1/1/2024', periods=5, freq='D')

data = {'X': [1, 2, 3, 4, 5]}

df = pd.DataFrame(data, index=date_range)
filtered_df = df['2024-01-03':'2024-01-05']

print(filtered_df)

# Output:
#             X
# 2024-01-03  3
# 2024-01-04  4
# 2024-01-05  5