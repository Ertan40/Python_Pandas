# Exercise 7:
# Sort a DataFrame by a column.

import pandas as pd

data = {'X': [4, 2, 3, 1], 'Y': [5, 6, 7, 8], 'Z': [9, 10, 11, 12]}

df = pd.DataFrame(data)
df.sort_values(by='X', inplace=True)
print(df)