# Exercise 33:
# Change the data type of a column.


import pandas as pd

data = {'X': ['1', '2', '3']}

df = pd.DataFrame(data)

df['X'] = df['X'].astype(int)

print(df.dtypes)