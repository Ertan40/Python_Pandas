"""
Exercise 69:

Create a DataFrame and calculate the percentage of missing values in each column.
"""

import pandas as pd

data = {'A': [1, 2, None, 4], 'B': [5, None, 7, 8]}

df = pd.DataFrame(data)

missing_percentage = (df.isna().sum() / len(df)) * 100
# missing_percentage = df.isnull().mean() * 100

print(missing_percentage)

# Output:

# A    25.0
# B    25.0
# dtype: float64