"""
Exercise 46:

Calculate the percentage change between rows in a DataFrame.
"""

import pandas as pd

data = {'X': [1, 2, 3, 4]}

df = pd.DataFrame(data)

df['percentage_change'] = df['X'].pct_change()

print(df)

# Output:
#    X  percentage_change
# 0  1                NaN
# 1  2           1.000000
# 2  3           0.500000
# 3  4           0.333333