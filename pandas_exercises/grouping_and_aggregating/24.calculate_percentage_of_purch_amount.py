"""
24. Write a Pandas program to split the following datasets into groups on customer_id to summarize purch_amt and
calculate percentage of purch_amt in each group.
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

print("Original Orders DataFrame:")
print(df)

grouped_df = df.groupby('customer_id')['purch_amt'].sum().reset_index()
grouped_df.columns = ['customer_id', 'total_purch_amt']
print("\nSummarized Total Purchase Amount per Customer:")
print(grouped_df)

# Merge total purchase amount to the original df
df = df.merge(grouped_df, on='customer_id')

# Calculate percentage of each purchase amount in its respective customer group
df['purch_amt_pct'] = (df['purch_amt'] / df['total_purch_amt']) * 100

print("\nDataFrame with Percentage of Each Purchase Amount:")
print(df[['customer_id', 'salesman_id', 'purch_amt', 'purch_amt_pct']])

