"""
Write a Pandas program to split the following dataframe into groups by school code and get mean, min, and
max value of age with customized column name for each school.
"""

import pandas as pd


student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    ' height ': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

df = pd.DataFrame(student_data)
print(f"Original df: \n{df}")

print('\nMin, max, and mean value of age for each school with customized column names:')
df['min_age'] = df.groupby('school_code')['age'].transform('min')
df['max_age'] = df.groupby('school_code')['age'].transform('max')
df['mean_age'] = df.groupby('school_code')['age'].transform('mean')
result = df[['school_code', 'min_age', 'max_age', 'mean_age']].drop_duplicates()
# Or you can achieve same as below (second way)
# result = df.groupby('school_code').agg(min_age=('age', 'min'),
#                                               max_age=('age', 'max'),
#                                               mean_age=('age', 'mean'))
print(result)

# Output:
# Original df:
#    school_code class            name  ...  height   weight  address
# S1        s001     V  Alberto Franco  ...      173      35  street1
# S2        s002     V    Gino Mcneill  ...      192      32  street2
# S3        s003    VI     Ryan Parkes  ...      186      33  street3
# S4        s001    VI    Eesha Hinton  ...      167      30  street1
# S5        s002     V    Gino Mcneill  ...      151      31  street2
# S6        s004    VI    David Parkes  ...      159      32  street4
#
# [6 rows x 8 columns]
#
# Min, max, and mean value of age for each school with customized column names:
#    school_code  min_age  max_age  mean_age
# S1        s001       12       13      12.5
# S2        s002       12       14      13.0
# S3        s003       13       13      13.0
# S6        s004       12       12      12.0
