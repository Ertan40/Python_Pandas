# Exercise 3:
# Select the 'X' column from a DataFrame.

import pandas as pd

data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}

df = pd.DataFrame(data)

print(df['X'])