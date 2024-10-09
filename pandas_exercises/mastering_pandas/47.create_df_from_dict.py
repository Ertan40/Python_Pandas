"""
Exercise 47:

Create a DataFrame from a dictionary of Series.
"""

import pandas as pd

data = {'X': pd.Series([1, 2, 3]), 'Y': pd.Series([4, 5, 6])}

df = pd.DataFrame(data)

print(df)

# Output:
#    X  Y
# 0  1  4
# 1  2  5
# 2  3  6