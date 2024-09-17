# Exercise 19:
# Iterate over rows in a DataFrame using iterrows().

import pandas as pd
data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}

df = pd.DataFrame(data)

for index, row in df.iterrows():
    print(index, row['X'], row['Y'])