"""
7. Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group. Using the
following dataset find the mean, min, and max values of purchase amount (purch_amt) group by customer id (customer_id).
"""

import pandas as pd

pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
orders_data = pd.DataFrame({
    'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10',
                 '2012-10-10',
                 '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3005, 3001, 3002, 3009, 3005, 3007, 3002, 3004, 3009, 3008, 3003, 3002],
    'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]})

print("Original dataframe:")
print(orders_data)


result = orders_data.groupby('customer_id').agg({'purch_amt': ['mean', 'min', 'max']})
print("\nMean, min, and max values of purchase amount (purch_amt) group by customer id  (customer_id).")
print(result)

# Output - result part:
# Mean, min, and max values of purchase amount (purch_amt) group by customer id  (customer_id).
#                purch_amt
#                     mean      min      max
# customer_id
# 3001          270.650000   270.65   270.65
# 3002         2956.953333    65.26  5760.00
# 3003           75.290000    75.29    75.29
# 3004         1983.430000  1983.43  1983.43
# 3005          549.500000   150.50   948.50
# 3007         2400.600000  2400.60  2400.60
# 3008          250.450000   250.45   250.45
# 3009         1295.450000   110.50  2480.40
