"""
28. Write a Pandas program to split a given dataset, group by one column and remove those groups
if all the values of a specific columns are not available.
"""

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'weight': [173, 192, 186, 167, 151, 159],
    'height': [35, None, 33, 30, None, 32]},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

print("Original DataFrame:")
print(df)

print("\nGroup by one column and remove those groups if all the values of a specific columns are not available:")
new_df = df[(~df['height'].isna()).groupby(df['school_code']).transform('any')]

print(new_df)

# Output:

# Original DataFrame:
#    school_code class            name date_Of_Birth   age  weight  height
# S1        s001     V  Alberto Franco     15/05/2002   12     173    35.0
# S2        s002     V    Gino Mcneill     17/05/2002   12     192     NaN
# S3        s003    VI     Ryan Parkes     16/02/1999   13     186    33.0
# S4        s001    VI    Eesha Hinton     25/09/1998   13     167    30.0
# S5        s002     V    Gino Mcneill     11/05/2002   14     151     NaN
# S6        s004    VI    David Parkes     15/09/1997   12     159    32.0
#
# Group by one column and remove those groups if all the values of a specific columns are not available:
#    school_code class            name date_Of_Birth   age  weight  height
# S1        s001     V  Alberto Franco     15/05/2002   12     173    35.0
# S3        s003    VI     Ryan Parkes     16/02/1999   13     186    33.0
# S4        s001    VI    Eesha Hinton     25/09/1998   13     167    30.0
# S6        s004    VI    David Parkes     15/09/1997   12     159    32.0