"""
Exercise 56:

Create a DataFrame and calculate the rolling standard deviation.
"""

import pandas as pd
data = {'X': [1, 2, 3, 4, 5, 6]}

df = pd.DataFrame(data)

df['Rolling Standard'] = df['X'].rolling(window=3).std()

print(df)

# Output:
#    X  Rolling Standard
# 0  1               NaN
# 1  2               NaN
# 2  3               1.0
# 3  4               1.0
# 4  5               1.0
# 5  6               1.0