"""
Exercise 68:

Create a DataFrame with hierarchical index and calculate the mean for each group.
"""

import pandas as pd
arrays = [['X', 'X', 'Y', 'Y'], [1, 2, 1, 2]]

index = pd.MultiIndex.from_arrays(arrays, names=('Group', 'Number'))

data = {'Value': [10, 20, 30, 40]}

df = pd.DataFrame(data=data, index=index)

grouped_df = df.groupby('Group').mean()

print(grouped_df)

# Output:
#        Value
# Group
# X       15.0
# Y       35.0