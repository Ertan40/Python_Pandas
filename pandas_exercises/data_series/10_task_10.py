## Write a Pandas program to convert Series of lists to one Series.
# Sample Output:
# Original Series of list
# 0    [Red, Green, White]
# 1           [Red, Black]
# 2               [Yellow]
# dtype: object

import pandas as pd

s1 = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ["Yellow"]])
print(f"Original Series of list: \n{s1}")

s1 = s1.apply(pd.Series).stack().reset_index(drop=True)
print(f"one Series: \n{s1}")