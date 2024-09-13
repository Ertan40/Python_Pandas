# Exercise 16:
# Create a pivot table from a DataFrame.

import pandas as pd
data = {'X': ['foo', 'foo', 'bar', 'bar'], 'Y': ['one', 'two', 'one', 'two'], 'Z': [1, 2, 3, 4]}
df = pd.DataFrame(data)

# pivot_table = df.pivot_table(index=['X', 'Y'], values='Z')
pivot_table = df.pivot_table(index='X', values='Z', columns='Y')

print(pivot_table)