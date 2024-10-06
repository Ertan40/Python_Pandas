# Exercise 36:
# Transpose a DataFrame.

import pandas as pd

data = {'X': [1, 2, 3], 'Y': [4, 5, 6]}

df = pd.DataFrame(data)

transposed_df = df.transpose()

print(transposed_df)

# Output:
#    0  1  2
# X  1  2  3
# Y  4  5  6