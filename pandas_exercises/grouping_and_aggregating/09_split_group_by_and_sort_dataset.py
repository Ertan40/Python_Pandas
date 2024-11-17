"""
9. Write a Pandas program to split a dataset to group by two columns and then sort the aggregated results within
the groups. In the following dataset group on 'customer_id', 'salesman_id' and
then sort sum of purch_amt within the groups.
"""

import pandas as pd

pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

df = pd.DataFrame({
    'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10',
                 '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3001, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3005],
    'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]})

print("Original Orders DataFrame:")
print(df)

df_agg = df.groupby(['customer_id', 'salesman_id']).sum()
result = df_agg['purch_amt'].groupby(level=0, group_keys=False)

print("\nGroup on 'customer_id', 'salesman_id' and then sort sum of purch_amt within the groups:")
print(result.nlargest())



# Output:
#
# Original Orders DataFrame:
#     ord_no  purch_amt    ord_date  customer_id  salesman_id
# 0    70001     150.50  2012-10-05         3001         5002
# 1    70009     270.65  2012-09-10         3001         5005
# 2    70002      65.26  2012-10-05         3005         5001
# 3    70004     110.50  2012-08-17         3001         5003
# 4    70007     948.50  2012-09-10         3005         5002
# 5    70005    2400.60  2012-07-27         3001         5001
# 6    70008    5760.00  2012-09-10         3005         5001
# 7    70010    1983.43  2012-10-10         3001         5006
# 8    70003    2480.40  2012-10-10         3005         5003
# 9    70012     250.45  2012-06-27         3001         5002
# 10   70011      75.29  2012-08-17         3005         5007
# 11   70013    3045.60  2012-04-25         3005         5001
#
# Group on 'customer_id', 'salesman_id' and then sort sum of purch_amt within the groups:
# customer_id  salesman_id
# 3001         5001           2400.60
#              5006           1983.43
#              5002            400.95
#              5005            270.65
#              5003            110.50
# 3005         5001           8870.86
#              5003           2480.40
#              5002            948.50
#              5007             75.29
# Name: purch_amt, dtype: float64