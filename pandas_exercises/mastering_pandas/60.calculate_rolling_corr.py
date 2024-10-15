"""
Exercise 60:

Create a DataFrame and calculate the rolling correlation between two columns.
"""

import pandas as pd
data = {'X': [1, 2, 3, 4, 5, 6], 'Y': [6, 5, 4, 3, 2, 1]}
df = pd.DataFrame(data)

df['Rolling_Correlation'] = df['X'].rolling(window=3).corr(df['Y'])

print(df)

# Output:
#    X  Y  Rolling_Correlation
# 0  1  6                  NaN
# 1  2  5                  NaN
# 2  3  4                 -1.0
# 3  4  3                 -1.0
# 4  5  2                 -1.0
# 5  6  1                 -1.0
#
# Process finished with exit code 0
