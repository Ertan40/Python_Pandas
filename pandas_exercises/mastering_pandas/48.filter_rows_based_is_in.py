"""
Exercise 48:

Filter rows based on whether a column value is in a list.
"""

import pandas as pd

data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}

df = pd.DataFrame(data)

filtered_df = df[df['X'].isin([2, 3])]

print(filtered_df)

# Output:
#    X  Y
# 1  2  6
# 2  3  7