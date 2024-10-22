"""
Exercise 65:

Create a DataFrame and calculate the z-score of each column.
"""

import pandas as pd
import numpy as np

# print([i for i in range(1, 5)])
# print([i for i in range(4, 8)])

data = {'X': [1, 2, 3, 4], 'Y': [4, 5, 6, 7]}

df = pd.DataFrame(data)

df['Z-Score_A'] = (df['X'] - np.mean(df['X']) / np.std(df['X']))
df['Z-Score_B'] = (df['Y'] - np.mean(df['Y']) / np.std(df['Y']))

print(df)

# Output:
#    X  Y  Z-Score_A  Z-Score_B
# 0  1  4  -1.236068   -0.91935
# 1  2  5  -0.236068    0.08065
# 2  3  6   0.763932    1.08065
# 3  4  7   1.763932    2.08065