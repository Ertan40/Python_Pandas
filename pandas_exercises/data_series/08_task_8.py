## Write a Pandas program to convert the first column of a DataFrame as a Series.
# Original DataFrame
#    col1  col2  col3
# 0     1     4     7
# 1     2     5     5
# 2     3     6     8
# 3     4     9    12
# 4     7     5     1
# 5    11     0    11

import pandas as pd

d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)

print(f"Original DataFrame: \n{df}")

s1 = df.iloc[:, 0]   # s1 = df['col1']  # or the column by name
print(f"1st column as a Series: \n{s1}")
print(type(s1))
