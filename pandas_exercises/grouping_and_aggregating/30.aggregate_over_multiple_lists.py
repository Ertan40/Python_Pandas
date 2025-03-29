"""
30. Write a Pandas program to split the following dataset using group by on first column
and aggregate over multiple lists on second column.
"""

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.DataFrame({
    'student_id': ['S001', 'S001', 'S002', 'S002', 'S003', 'S003'],
    'marks': [[88, 89, 90], [78, 81, 60], [84, 83, 91], [84, 88, 91], [90, 89, 92], [88, 59, 90]]})

print("Original DataFrame:")
print(df)

new_df = df.set_index('student_id')['marks'].groupby('student_id').apply(list).apply(lambda x: np.mean(x,0))

print("\nGroup by and aggregate over multiple lists:")
print(new_df)

# Output:
# Original DataFrame:
#   student_id         marks
# 0       S001  [88, 89, 90]
# 1       S001  [78, 81, 60]
# 2       S002  [84, 83, 91]
# 3       S002  [84, 88, 91]
# 4       S003  [90, 89, 92]
# 5       S003  [88, 59, 90]
#
# Groupby and aggregate over multiple lists:
# student_id
# S001    [83.0, 85.0, 75.0]
# S002    [84.0, 85.5, 91.0]
# S003    [89.0, 74.0, 91.0]
# Name: marks, dtype: object

