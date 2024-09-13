# Exercise 13:
# Calculate the mean of values in each row.

import pandas as pd

data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}

df = pd.DataFrame(data)

print(df.mean(axis=1))