# Exercise 34:
# Filter rows based on string matching.

import pandas as pd
data = {'X': ['foo', 'bar', 'baz', 'qux']}

df = pd.DataFrame(data)

filtered_df = df[df['X'].str.contains('ba')]

print(filtered_df)