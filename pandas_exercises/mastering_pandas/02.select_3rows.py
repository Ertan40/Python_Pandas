# Exercise 2:
# Select the first 3 rows of a DataFrame.

import pandas as pd

data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}

df = pd.DataFrame(data)

print(df.head(3))