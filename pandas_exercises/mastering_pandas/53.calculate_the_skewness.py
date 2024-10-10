"""
Exercise 53:

Create a DataFrame with random values and calculate the skewness.
"""

import pandas as pd
import numpy as np

data = np.random.rand(4, 3)  # 4 rows and 3 columns of random values

df = pd.DataFrame(data, columns=['X', 'Y', 'Z'])

print(df.skew())
