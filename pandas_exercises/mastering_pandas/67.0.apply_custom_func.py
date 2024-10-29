"""
Exercise 67:

Create a DataFrame and apply a custom function to each column.
"""

import pandas as pd

data = {'A': [1, 2, 3, 4], 'B': [4, 5, 6, 7]}

df = pd.DataFrame(data)

df = df.apply(lambda x: x + 1)

print(df)

# Output:
#   A  B
# 0  2  5
# 1  3  6
# 2  4  7
# 3  5  8