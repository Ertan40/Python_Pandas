# Remove a column from a DataFrame

import pandas as pd

data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8], 'Z': [9, 10, 11, 12]}

df = pd.DataFrame(data)
remove_col = df.drop(columns='Z', inplace=True)

print(df)