## Write a Pandas program to convert a Panda module Series to Python list and it's type.

import pandas as pd

numbers = list(range(1, 11))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

ds = pd.Series(even_numbers)
print(f"Pandas series and type: \n{ds}")
print(type(ds))
print("Convert Pandas Series to Python List")
print(ds.tolist())
print(type(ds.tolist()))
