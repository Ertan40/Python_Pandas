"""
Exercise 61:

Create a DataFrame and calculate the expanding variance.
"""

import pandas as pd

data = {'X': [1, 2, 3, 4, 5, 6]}

df = pd.DataFrame(data)

df['Expanding Variance'] = df['X'].expanding().var()

print(df)

# Output:
#    X  Expanding Variance
# 0  1                 NaN
# 1  2            0.500000
# 2  3            1.000000
# 3  4            1.666667
# 4  5            2.500000
# 5  6            3.500000


