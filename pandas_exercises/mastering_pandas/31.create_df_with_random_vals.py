# Exercise 31:
# Create a DataFrame with random values.

import pandas as pd
import numpy as np

data = np.random.rand(4, 3)
df = pd.DataFrame(data, columns=['X', 'Y', 'Z'])

print(round(df, 2))