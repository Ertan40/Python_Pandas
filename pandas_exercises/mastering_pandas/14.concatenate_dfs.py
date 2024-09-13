# Exercise 14:
# Concatenate two DataFrames.

import pandas as pd
data1 = {'X': [1, 2, 3]}
data2 = {'Y': [4, 5, 6]}

df_1 = pd.DataFrame(data1)
df_2 = pd.DataFrame(data2)

df = pd.concat([df_1, df_2], axis=1)
print(df)