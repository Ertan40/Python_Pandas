"""
Exercise 57:

Create a DataFrame and calculate the expanding mean.
"""

import pandas as pd

data = {'X': [1, 2, 3, 4, 5, 6]}

df = pd.DataFrame(data)

df['Expanding mean'] = df['X'].expanding().mean()

print(df)

# Output:
#    X  Expanding mean
# 0  1             1.0
# 1  2             1.5
# 2  3             2.0
# 3  4             2.5
# 4  5             3.0
# 5  6             3.5