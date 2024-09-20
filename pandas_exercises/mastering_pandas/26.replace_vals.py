# Exercise 25:
# Replace values in a DataFrame based on a condition.

import pandas as pd
data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}

df = pd.DataFrame(data)

df_replaced = df.replace(2, 82)
print(df_replaced)

# Based on condition

df.loc[df['X'] > 2, 'Y'] = 0
print(df)