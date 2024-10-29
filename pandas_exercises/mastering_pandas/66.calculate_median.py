"""
Exercise 66:

Create a DataFrame with random values and calculate the median.
"""

import pandas as pd
import numpy as np

data = np.random.rand(4, 3)

df = pd.DataFrame(data=data, columns=['A', 'B', 'C'])


print(df.median())

# Output:
# A    0.347010
# B    0.288989
# C    0.407403
# dtype: float64