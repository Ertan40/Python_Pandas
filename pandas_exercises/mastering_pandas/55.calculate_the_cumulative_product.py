"""
Exercise 55:

Calculate the cumulative product of a column in a DataFrame.
"""

import pandas as pd
data = {'X': [1, 2, 3, 4]}

df = pd.DataFrame(data)

df['Cumulative product'] = df['X'].cumprod()

print(df)

# Output:
#    X  Cumulative product
# 0  1                   1
# 1  2                   2
# 2  3                   6
# 3  4                  24