# Exercise 20:
# Apply a function to each element in a DataFrame.

import pandas as pd

data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}
df = pd.DataFrame(data)

applied_df = df.apply(lambda col: col.map(lambda x: x*2))

print(applied_df)