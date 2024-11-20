"""
Write a Pandas program to split the following dataframe into groups based on all columns and calculate GroupBy
value counts on the dataframe.

Test Data:

   id  type     book
0   1    10     Math
1   2    15  English
2   1    11  Physics
3   1    20     Math
4   2    21  English
5   1    12  Physics
6   2    14  English
"""

import pandas as pd

data = {"id": [1, 2, 1, 1, 2, 1, 2],
        "type": [10, 15, 11, 20, 21, 12, 14],
        "book": ['Math', 'English', 'Physics', 'Math', 'English', 'Physics', 'English']}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

result = df.groupby(['id', 'type', 'book']).size().unstack(fill_value=0)

print("\nResult:")
print(result)

# Output:
# Original DataFrame:
#    id  type     book
# 0   1    10     Math
# 1   2    15  English
# 2   1    11  Physics
# 3   1    20     Math
# 4   2    21  English
# 5   1    12  Physics
# 6   2    14  English
#
# Result:
# book     English  Math  Physics
# id type
# 1  10          0     1        0
#    11          0     0        1
#    12          0     0        1
#    20          0     1        0
# 2  14          1     0        0
#    15          1     0        0
#    21          1     0        0