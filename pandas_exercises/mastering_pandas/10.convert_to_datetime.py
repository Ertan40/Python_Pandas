# Exercise 10:
# Convert a column to datetime.

import pandas as pd
data = {'X': ['2020-01-01', '2020-01-02', '2020-01-03']}
df = pd.DataFrame(data)

df['X'] = pd.to_datetime(df['X'])
print(df)