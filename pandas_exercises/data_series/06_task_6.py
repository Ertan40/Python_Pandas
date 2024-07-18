## Write a Pandas program to convert a NumPy array to a Pandas series.
## NumPy array: [10 20 30 40 50]

import pandas as pd
import numpy as np

numpy_array = np.array([num for num in range(10, 51, 10)])
# print(numpy_array)

ds = pd.Series(numpy_array)
print(f"Converted Pandas series: \n{ds}")