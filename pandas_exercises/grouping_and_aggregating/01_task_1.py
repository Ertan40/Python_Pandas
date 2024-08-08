## 1. Write a Pandas program to split the following dataframe into groups based on school code.
# Also check the type of GroupBy object.
# Test Data:
#    school class            name date_Of_Birth   age  height  weight  address
# S1   s001     V  Alberto Franco     15/05/2002   12    173      35  street1
# S2   s002     V    Gino Mcneill     17/05/2002   12    192      32  street2
# S3   s003    VI     Ryan Parkes     16/02/1999   13    186      33  street3
# S4   s001    VI    Eesha Hinton     25/09/1998   13    167      30  street1
# S5   s002     V    Gino Mcneill     11/05/2002   14    151      31  street2
# S6   s004    VI    David Parkes     15/09/1997   12    159      32  street4

import pandas as pd
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

print('Original data')
print(student_data)
print('\nSplit the said data on school_code wise:')
result = student_data.groupby(['school_code'])
for name, group in result:
    print('\nGroup:')
    print(name)
    print(group)

print("\nType of the object:")
print(type(result))