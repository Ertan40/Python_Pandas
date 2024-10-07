"""
Exercise 45:

Filter rows based on the length of strings in a column.
"""

import pandas as pd

data = {'X': ['foo', 'bar', 'baz', 'qux']}

df = pd.DataFrame(data)

filter_df = df[df['X'].str.len() > 3]

print(filter_df)

# Output
# Empty DataFrame
# Columns: [X]
# Index: []