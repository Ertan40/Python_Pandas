"""
Exercise 67:

Create a DataFrame and apply a custom function to a single column.
"""

import pandas as pd

data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}

df = pd.DataFrame(data)

# Method 1: Using apply() on a single column
# df['A'] = df['A'].apply(lambda x: x + 2)

# Method 2: Using map() on a single column
df['A'] = df['A'].map(lambda x: x + 2)

# Method 3: Using transform() on a single column
# df['A'] = df['A'].transform(lambda x: x + 2)

# Method 4: Using numpy operations
# df['A'] = df['A'] + 2

# Method 5: Using loc accessor
# df.loc[:, 'A'] = df['A'] + 2

print(df)

# Output:
# 0  3  5
# 1  4  6
# 2  5  7
# 3  6  8