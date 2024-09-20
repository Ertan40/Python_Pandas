# Exercise 29:
# Create a DataFrame from a list of tuples.

import pandas as pd
data = [(1, 2), (3, 4), (5, 6)]

df = pd.DataFrame(data, columns=['X', 'Y'])

print(df)