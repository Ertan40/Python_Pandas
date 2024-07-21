# Write a Pandas program to select the specified columns and rows from a given data frame.
# Sample Python dictionary data and list labels:
# Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.

import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

# print(df[['name', 'score']])
# iloc() function is used to select specific rows and columns from the DataFrame based on their integer location.
print(f"Select specific columns and rows: \n{df.iloc[[1, 3, 5, 6], [1, 3]]}")