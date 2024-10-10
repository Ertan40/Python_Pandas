"""
Exercise 51:

Calculate the rank of values in each column of a DataFrame.
"""


import pandas as pd

data = {'X': [3, 1, 4, 1], 'Y': [2, 3, 1, 4]}

df = pd.DataFrame(data)

df['rank_a'] = df['X'].rank()
df['rank_b'] = df['Y'].rank()

print(df)

# output:
#    X  Y  rank_a  rank_b
# 0  3  2     3.0     2.0
# 1  1  3     1.5     3.0
# 2  4  1     4.0     1.0
# 3  1  4     1.5     4.0