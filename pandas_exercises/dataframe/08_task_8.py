# Write a Pandas program to count the number of rows and columns of a DataFrame.
# Sample Python dictionary data and list labels:

import pandas as pd
import numpy as np


exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

# or via df.axes and len
# total_rows=len(df.axes[0])
# total_cols=len(df.axes[1])
# in order to get the shape of DF
rows, columns = df.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")
# print(f"Number of columns: {len(df.axes[1])}")