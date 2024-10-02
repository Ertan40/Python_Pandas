# Exercise 32:
# Calculate the rank of values in a DataFrame.

import pandas as pd
data = {'X': [3, 1, 4, 1], 'Y': [2, 3, 1, 4]}

df = pd.DataFrame(data)

df['Rank'] = df['X'].rank()
print(df)