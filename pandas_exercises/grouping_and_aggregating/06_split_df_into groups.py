"""
6. Write a Pandas program to split the following given dataframe into groups based on school code and call a specific
group with the name of the group.
"""

import pandas as pd
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])


print(student_data)

grouped_df = student_data.groupby(['school_code'])
print("Call school code 's001':")
print(grouped_df.get_group(('s001',)))

print("Call school code 's002':")
print(grouped_df.get_group(('s002',)))