"""
Exercise 54:

Create a DataFrame and calculate the kurtosis.
"""

import pandas as pd

import numpy as np

data = np.random.rand(4, 3)  # 4 rows and 3 columns of random values

df = pd.DataFrame(data, columns=['X', 'Y', 'Z'])

print(df.kurtosis())

# Output:
# X    1.750564
# Y    0.398756
# Z    1.978432
# dtype: float64