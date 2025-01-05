"""
Write a Pandas program to split the following dataframe into groups and calculate quarterly purchase amount.
"""

import pandas as pd

pd.set_option('display.max_rows', None)

df = pd.DataFrame({
    'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['05-10-2012', '09-10-2012', '05-10-2012', '08-17-2012', '10-09-2012', '07-27-2012', '10-09-2012',
                 '10-10-2012', '10-10-2012', '06-17-2012', '07-08-2012', '04-25-2012'],
    'customer_id': [3001, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3001, 3005, 3005],
    'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]})


print(f"Original df: \n{df}")

df['ord_date'] = pd.to_datetime(df['ord_date'], format='%m-%d-%Y')
# Create new col for the quarter
df['quarter'] = df['ord_date'].dt.to_period('Q')
# Group by the quarter and calculate the total purchase amount
quarterly_purchase = df.groupby('quarter')['purch_amt'].sum()
# Reset the index to get the clean df
quarterly_purchase = quarterly_purchase.reset_index()

quarterly_purchase.columns = ['quarter', 'total_purchase_amount']
print("\nQuarterly purchase amount:")
print(quarterly_purchase)

# Output:
# Original df:
#     ord_no  purch_amt    ord_date  customer_id  salesman_id
# 0    70001     150.50  05-10-2012         3001         5002
# 1    70009     270.65  09-10-2012         3001         5005
# 2    70002      65.26  05-10-2012         3005         5001
# 3    70004     110.50  08-17-2012         3001         5003
# 4    70007     948.50  10-09-2012         3005         5002
# 5    70005    2400.60  07-27-2012         3001         5001
# 6    70008    5760.00  10-09-2012         3005         5001
# 7    70010    1983.43  10-10-2012         3001         5006
# 8    70003    2480.40  10-10-2012         3005         5003
# 9    70012     250.45  06-17-2012         3001         5002
# 10   70011      75.29  07-08-2012         3005         5007
# 11   70013    3045.60  04-25-2012         3005         5001
#
# Quarterly purchase amount:
#   quarter  total_purchase_amount
# 0  2012Q2                3511.81
# 1  2012Q3                2857.04
# 2  2012Q4               11172.33