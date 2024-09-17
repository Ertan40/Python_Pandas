# Exercise 24:
# Calculate the cumulative sum of a column.

import pandas as pd
data = {'X': [1, 2, 3, 4]}

df = pd.DataFrame(data)
# sum_of_cols = df['X'].sum()
# print(sum_of_cols)  # 10

df['Cumulative_sum'] = df['X'].cumsum()
print(df)