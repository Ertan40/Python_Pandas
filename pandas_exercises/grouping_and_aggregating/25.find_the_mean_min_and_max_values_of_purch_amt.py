"""
25. Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group,
also change the column name of the aggregated metric.
"""

import pandas as pd

pd.set_option('display.max_rows', None)

df = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

print("Original DataFrame:")
print(df)

print('\nChange the name of an aggregated metric:')
grouped_df = df.groupby('school_code').agg({'age': [('mean_age', 'mean'), ('min_age', 'min'), ('max_age', 'max')]})

print(grouped_df)

# Output:

# Original DataFrame:
#    school_code class            name  ... height  weight  address
# S1        s001     V  Alberto Franco  ...    173      35  street1
# S2        s002     V    Gino Mcneill  ...    192      32  street2
# S3        s003    VI     Ryan Parkes  ...    186      33  street3
# S4        s001    VI    Eesha Hinton  ...    167      30  street1
# S5        s002     V    Gino Mcneill  ...    151      31  street2
# S6        s004    VI    David Parkes  ...    159      32  street4
#
# [6 rows x 8 columns]
#
# Change the name of an aggregated metric:
#                  age
#             mean_age min_age max_age
# school_code
# s001            12.5      12      13
# s002            13.0      12      14
# s003            13.0      13      13
# s004            12.0      12      12