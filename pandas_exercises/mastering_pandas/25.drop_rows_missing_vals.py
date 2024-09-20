# Exercise 25:
# Drop rows with missing values.

import pandas as pd

data = {'X': [1, 2, None, 4], 'Y': [4, 5, 6, None]}

df = pd.DataFrame(data)

df.dropna(inplace=True)

print(df)