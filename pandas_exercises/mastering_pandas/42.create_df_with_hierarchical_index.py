# Exercise 42:
# Create a DataFrame with hierarchical index.

import pandas as pd

arrays = [['X', 'X', 'Y', 'Y'], [1, 2, 1, 2]]

index = pd.MultiIndex.from_arrays(arrays, names=('Group', 'Number'))

data = {'Value': [10, 20, 30, 40]}

df = pd.DataFrame(data, index=index)

print(df)

# Output:
# Group Number
# X     1          10
#       2          20
# Y     1          30
#       2          40