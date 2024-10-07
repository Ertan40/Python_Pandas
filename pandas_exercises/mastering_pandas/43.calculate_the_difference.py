"""
Exercise 43:

Calculate the difference between consecutive rows in a DataFrame.
"""

import pandas as pd

data = {'X': [1, 3, 6, 10]}

df = pd.DataFrame(data)

df['Difference'] = df['X'].diff()

print(df)

# Output:
#     X  Difference
# 0   1         NaN
# 1   3         2.0
# 2   6         3.0
# 3  10         4.0