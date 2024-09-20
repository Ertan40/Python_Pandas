# Exercise 30:
# Add a row to a DataFrame.

import pandas as pd

data = {'X': [1, 2], 'Y': [3, 4]}

df = pd.DataFrame(data)

new_row = pd.DataFrame({'X': [5], 'Y': [6]})

# Concatenate
df = pd.concat([df, new_row], ignore_index=True)

print(df)