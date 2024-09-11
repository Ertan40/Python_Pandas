# Exercise 5:
# Add a new column to an existing DataFrame.

import pandas as pd

data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}

df = pd.DataFrame(data)
df['Z'] = df['X'] + df['Y']

print(df)