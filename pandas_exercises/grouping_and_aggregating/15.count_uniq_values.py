"""
15. Write a Pandas program to split the following dataframe into groups and count unique values of 'value' column.
Test Data:

   id value
0   1     a
1   1     a
2   2     b
3   3  None
4   3     a
5   4     a
6   4  None
7   4     b
"""

import pandas as pd
data = {"id": [1, 1, 2, 3, 3, 4, 4, 4],
        "value": ['a', 'a', 'b', None, 'a', 'a', None, 'b']}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("Count unique values:")
result = df.groupby('value')['id'].nunique()

print(result)

# Output:
# Original DataFrame:
#    id value
# 0   1     a
# 1   1     a
# 2   2     b
# 3   3  None
# 4   3     a
# 5   4     a
# 6   4  None
# 7   4     b
# Count unique values:
# value
# a    3
# b    2
# Name: id, dtype: int64