# Exercise 17:
# Reshape a DataFrame from long to wide format.

import pandas as pd
data = {'X': ['foo', 'foo', 'bar', 'bar'], 'Y': ['one', 'two', 'one', 'two'], 'Z': [1, 2, 3, 4]}
df = pd.DataFrame(data)

wide_df = df.pivot(index='X', values='Z', columns='Y')

print(wide_df)