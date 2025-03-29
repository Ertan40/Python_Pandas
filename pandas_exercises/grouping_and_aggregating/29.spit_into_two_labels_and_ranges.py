"""
29. Write a Pandas program to split a given dataset using group by on specified column into two labels and ranges.
"""

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.DataFrame({
    'salesman_id': [5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010, 5011, 5012],
    'sale_jan': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 1760, 2983.43, 480.4, 1250.45, 75.29, 1045.6]})

print("Original Orders DataFrame:")
print(df)

new_df = (df.groupby(pd.cut(df['salesman_id'], bins=[0, 5006, np.inf], labels=['S1', 'S2']))['sale_jan'].
          sum().reset_index())

print("\nGroupBy with condition of  two labels and ranges:")
print(new_df)
