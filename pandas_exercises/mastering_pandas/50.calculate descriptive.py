"""
Exercise 50:

Create a DataFrame with random integers and calculate descriptive statistics.
"""

import pandas as pd
import numpy as np

data = np.random.randint(1, 100, size=(5, 3))

df = pd.DataFrame(data, columns=['X', 'Y', 'Z'])

print(df.describe())

# Output:
#                X          Y          Z
# count   5.000000   5.000000   5.000000
# mean   42.400000  54.800000  49.800000
# std    36.732819  37.419246  27.298352
# min     6.000000   1.000000  16.000000
# 25%    15.000000  30.000000  31.000000
# 50%    30.000000  77.000000  48.000000
# 75%    69.000000  81.000000  76.000000
# max    92.000000  85.000000  78.000000


