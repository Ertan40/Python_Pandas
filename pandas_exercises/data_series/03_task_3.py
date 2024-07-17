## Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

import pandas as pd

ds_1 = pd.Series([2, 4, 6, 8, 10])
ds_2 = pd.Series([1, 3, 5, 7, 9])

add_series = ds_1 + ds_2
subtract_series = ds_1 - ds_2
multiply_series = ds_1 * ds_2
divide_series = ds_1 / ds_2
print(f"Add two Series: \n{add_series}")
print(f"Subtract two Series: \n{subtract_series}")
print(f"Multiply two Series: \n{multiply_series}")
print(f"Divide Series1 by Series2:: \n{divide_series}")