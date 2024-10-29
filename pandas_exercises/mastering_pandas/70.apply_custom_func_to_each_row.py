"""
Exercise 70:

Create a DataFrame and apply a custom function to each row.
"""

import pandas as pd

# A = [n for n in range(1, 5)]
# B = [n for n in range(6, 10)]
#
# print(A)
# print(B)

data = {'A': [1, 2, 3, 4], 'B': [6, 7, 8, 9]}

df = pd.DataFrame(data)

df['Sum_rows'] = df.apply(lambda x: x['A'] + x['B'], axis=1)

print(df)

# Output:
#    A  B  Sum_rows
# 0  1  6         7
# 1  2  7         9
# 2  3  8        11
# 3  4  9        13