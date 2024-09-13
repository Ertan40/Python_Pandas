# Exercise 12:
# Calculate the sum of values in each column.

import pandas as pd
data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}
df = pd.DataFrame(data)


print(df.sum())