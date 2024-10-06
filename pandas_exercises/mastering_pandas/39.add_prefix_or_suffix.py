# Exercise 39:
# Add a prefix or suffix to column names.


import pandas as pd
data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}

df = pd.DataFrame(data)

df = df.add_prefix('col_')

print(df)

# Output
#    col_X  col_Y
# 0      1      4
# 1      2      5
# 2      3      6