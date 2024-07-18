## Write a Pandas program to convert a dictionary to a Pandas series.
## origin_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

import pandas as pd

origin_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

print(f"Original dictionary: \n{origin_dict}")

new_series = pd.Series(origin_dict)
print(f"Converted series: \n{new_series}")
