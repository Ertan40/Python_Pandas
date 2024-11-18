"""
13. Write a Pandas program to split the following dataframe into groups based
on first column and set other column values into a list of values.
"""

import pandas as pd
df = pd.DataFrame({'X': [10, 10, 10, 20, 30, 30, 10],
                   'Y': [10, 15, 11, 20, 21, 12, 14],
                   'Z': [22, 20, 18, 20, 13, 10, 0]})

print("Original DataFrame:")
print(df)

result = df.groupby('X').aggregate(lambda tdf: tdf.unique().tolist())
print("\nGrouped and Aggregated DataFrame:")
print(result)

# Output:
# Original DataFrame:
#     X   Y   Z
# 0  10  10  22
# 1  10  15  20
# 2  10  11  18
# 3  20  20  20
# 4  30  21  13
# 5  30  12  10
# 6  10  14   0
#
# Grouped and Aggregated DataFrame:
#                    Y                Z
# X
# 10  [10, 15, 11, 14]  [22, 20, 18, 0]
# 20              [20]             [20]
# 30          [21, 12]         [13, 10]





