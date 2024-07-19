## Write a Pandas program to change the data type of given a column or a Series.
# Sample Series:
# Original Data Series:
# 0 100
# 1 200
# 2 python
# 3 300.12
# 4 400
# dtype: object

import pandas as pd

s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print(f"Original Data Series: \n{s1}")

s2 = pd.to_numeric(s1, errors='coerce')
print(f"Change to Numeric: \n{s2}" )