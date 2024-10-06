# Exercise 38:
# Reset the index of a DataFrame.

import pandas as pd
data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}

df = pd.DataFrame(data)

df.set_index('X', inplace=True)
df.reset_index(inplace=True)

print(df)

# output:
#    X  Y
# 0  1  4
# 1  2  5
# 2  3  6
