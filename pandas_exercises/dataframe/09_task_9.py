# Write a Pandas program to select the rows where the score is missing, i.e. is NaN.
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

# Both pd.isna() and isnull() are designed to work with NaN values
print(f"Rows where score is missing: \n{df[pd.isna(df['score'])]}")
# or as below:
# print(f"Rows where score is missing: \n{df[df['score'].isnull()]}")
