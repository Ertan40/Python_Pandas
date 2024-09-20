# Exercise 28:
# Calculate the rolling mean of a column.

import pandas as pd
data = {'X': [1, 2, 3, 4, 5, 6]}

df = pd.DataFrame(data)

df['rolling_mean'] = df['X'].rolling(window=3).mean()
print(df)