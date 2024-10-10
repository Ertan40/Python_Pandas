"""
Exercise 52:

Filter rows based on multiple string conditions.
"""

import pandas as pd

data = {'X': ['foo', 'bar', 'baz', 'qux']}

df = pd.DataFrame(data)

filtered_df = df[df['X'].str.contains('ba|qu')]

print(filtered_df)

# Output:
#      X
# 1  bar
# 2  baz
# 3  qux