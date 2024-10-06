# Exercise 37:
# Set a column as the index of a DataFrame.

import pandas as pd
data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}

df = pd.DataFrame(data)

df.set_index('X', inplace=True)

print(df)

# Output:
#    Y
# X
# 1  4
# 2  5
# 3  6