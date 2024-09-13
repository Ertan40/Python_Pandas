# Exercise 18:
# Calculate the correlation between columns in a DataFrame.

import pandas as pd
data = {'X': [1, 2, 3, 4], 'Y': [4, 3, 2, 1]}
df = pd.DataFrame(data)

correlation = df.corr()

print(correlation)