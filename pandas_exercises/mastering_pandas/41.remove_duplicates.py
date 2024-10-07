# Exercise 41:
# Create a DataFrame with duplicate rows and remove duplicates.

import pandas as pd

data = {'X': [3, 1, 4, 1, 5], 'Y': [2, 3, 1, 3, 6]}

df = pd.DataFrame(data)

df.drop_duplicates(inplace=True)

print(df)

# Output:
#    X  Y
# 0  3  2
# 1  1  3
# 2  4  1
# 4  5  6