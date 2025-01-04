"""
Write a Pandas program to split a given dataframe into groups and display target column as a list of unique values.

Test Data:

   id  type     book
0   A     1     Math
1   A     1     Math
2   A     1  English
3   A     1  Physics
4   A     2     Math
5   A     2  English
6   B     1  Physics
7   B     1  English
8   B     1  Physics
9   B     2  English
10  B     2  English
"""

import pandas as pd

df = pd.DataFrame({'id': ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
                   'type': [1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2],
                   'book': ['Math', 'Math', 'English', 'Physics', 'Math', 'English', 'Physics', 'English', 'Physics',
                            'English', 'English']})


print(f"Original df: \n{df}")

new_df = df[["id", "type", "book"]].drop_duplicates()\
    .groupby(["id", "type"])["book"]\
    .apply(list)\
    .reset_index()

# print(new_df)
#   id  type                      book
# 0  A     1  [Math, English, Physics]
# 1  A     2           [Math, English]
# 2  B     1        [Physics, English]
# 3  B     2                 [English]
new_df["book"] = new_df.apply(lambda x: ', '.join([str(x) for x in x["book"]]), axis=1)

print(f"List all unique values in a group: \n{new_df}")

# Output:
# Original df:
#    id  type     book
# 0   A     1     Math
# 1   A     1     Math
# 2   A     1  English
# 3   A     1  Physics
# 4   A     2     Math
# 5   A     2  English
# 6   B     1  Physics
# 7   B     1  English
# 8   B     1  Physics
# 9   B     2  English
# 10  B     2  English
# List all unique values in a group:
#   id  type                    book
# 0  A     1  Math, English, Physics
# 1  A     2           Math, English
# 2  B     1        Physics, English
# 3  B     2                 English