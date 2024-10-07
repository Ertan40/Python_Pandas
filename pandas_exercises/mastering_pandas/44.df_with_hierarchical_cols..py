"""
Exercise 44:

Create a DataFrame with hierarchical columns.
"""

import pandas as pd


arrays = [['X', 'X', 'Y', 'Y'], ['C1', 'C2', 'C1', 'C2']]

columns = pd.MultiIndex.from_arrays(arrays, names=('Group', 'Type'))

data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

df = pd.DataFrame(data, columns=columns)

print(df)

# Output
# Group  X       Y
# Type  C1  C2  C1  C2
# 0      1   2   3   4
# 1      5   6   7   8
# 2      9  10  11  12