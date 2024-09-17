# Exercise 21:
# Create a DataFrame from a list of dictionaries.

import pandas as pd

data = [{'X': 1, 'Y': 2}, {'X': 3, 'Y': 4}]

df = pd.DataFrame(data)

print(df)