# Exercise 8:
# Group a DataFrame by a column and calculate the mean of each group.

import pandas as pd
data = {'X': [1, 2, 1, 2], 'Y': [5, 6, 7, 8]}

df = pd.DataFrame(data)
group_df = df.groupby('X').mean()

print(group_df)