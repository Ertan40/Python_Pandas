# Exercise 9:
# Replace missing values in a DataFrame.

import pandas as pd

data = {'X': [1, 2, None, 4], 'Y': [5, None, 7, 8]}

df = pd.DataFrame(data)

df.fillna(0, inplace=True)

print(df)