## Write a Pandas program to convert a given Series to an array.
# Sample Output:
# Original Data Series:
# 0       100
# 1       200
# 2    python
# 3    300.12
# 4       400
# dtype: object

import pandas as pd
import numpy as np

s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print(f"Original Data Series: \n{s1}")

a = np.array(s1.values.tolist())
print(f"Convert to an array: \n{a}")
print(type(a))