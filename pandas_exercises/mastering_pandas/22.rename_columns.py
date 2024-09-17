# Exercise 22:
# Rename columns in a DataFrame

import pandas as pd
data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}

df = pd.DataFrame(data)

df.rename(columns={'X': 'A', 'Y': 'B'}, inplace=True)

print(df)