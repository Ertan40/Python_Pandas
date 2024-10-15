"""
Exercise 59:

Create a DataFrame with random values and calculate the correlation matrix.
"""

import pandas as pd
import numpy as np

random_values = np.random.rand(4, 3)

df = pd.DataFrame(random_values, columns=['X', 'Y', 'Z'])

print(df.corr())

# Output:
#           X         Y         Z
# X  1.000000 -0.883537 -0.373283
# Y -0.883537  1.000000  0.518703
# Z -0.373283  0.518703  1.000000