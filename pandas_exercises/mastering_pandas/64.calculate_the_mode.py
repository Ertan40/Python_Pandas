"""
Exercise 64:

Create a DataFrame with random integers and calculate the mode
"""

import pandas as pd
import numpy as np

data = np.random.randint(1, 10, size=(5, 3))

df = pd.DataFrame(data=data, columns=['X', 'Y', 'Z'])

print(df.mode())

# Output:
#    X    Y    Z
# 0  2  1.0  9.0
# 1  3  8.0  NaN
# 2  4  NaN  NaN
# 3  6  NaN  NaN
# 4  7  NaN  NaN