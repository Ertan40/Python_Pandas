"""
Exercise 49:

Calculate the z-score of values in a DataFrame
"""

import pandas as pd
import numpy as np

data = {'X': [1, 2, 3, 4], 'Y': [4, 5, 6, 7]}

df = pd.DataFrame(data)

df['Z-Score_A'] = (df['X'] - np.mean(df['X'])) / np.std(df['X'])

print(df)

# Output:
#    X  Y  Z-Score_A
# 0  1  4  -1.341641
# 1  2  5  -0.447214
# 2  3  6   0.447214
# 3  4  7   1.341641