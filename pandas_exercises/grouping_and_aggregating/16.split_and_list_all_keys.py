"""
Write a Pandas program to split a given dataframe into groups and list all the keys from the GroupBy object.
"""

import pandas as pd
pd.set_option('display.max_rows', None)

df = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

print("Original DataFrame:")
print(df)

result = df.groupby('school_code')
print("\nList of all the keys:")
print(result.groups.keys())

# Output
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
# List of all the keys:
# dict_keys(['s001', 's002', 's003', 's004'])