## Write a Pandas program to create and display a one-dimensional array-like object containing an array of data.

import pandas as pd

numbers = list(range(11))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# even_numbers = [x for x in numbers if x % 2 == 0]

ds = pd.Series(even_numbers)
print(ds)

