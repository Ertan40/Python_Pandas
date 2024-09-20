# Exercise 27:
# Create a DataFrame with a MultiIndex.

import pandas as pd
arrays = [['X', 'X', 'Y', 'Y'], [1, 2, 1, 2]]

index = pd.MultiIndex.from_arrays(arrays, names=('Group', 'Number'))

data = {'Value': [10, 20, 30, 40]}

df = pd.DataFrame(data, index=index)
print(df)