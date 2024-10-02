# Exercise 35:
# Create a DataFrame with specified row and column labels.

import pandas as pd
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

df = pd.DataFrame(data, index=['row1', 'row2', 'row3'], columns=['col1', 'col2', 'col3'])

print(df)

# Output
#       col1  col2  col3
# row1     1     2     3
# row2     4     5     6
# row3     7     8     9