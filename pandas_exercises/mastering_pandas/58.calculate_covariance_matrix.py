"""
Exercise 58:

Create a DataFrame with random values and calculate the covariance matrix.
"""

import pandas as pd
import numpy as np

random_values = np.random.rand(4, 3)  # np.random.rand(rows, cols)

df = pd.DataFrame(random_values, columns=['X', 'Y', 'Z'])

df.cov()

print(round(df, 2))

# Output:
#       X     Y     Z
# 0  0.56  0.63  0.88
# 1  0.91  1.00  0.05
# 2  0.21  0.56  0.79
# 3  0.39  0.16  0.35