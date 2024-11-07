"""
8. Write a Pandas program to split a dataset to group by two columns and count by each row.
"""
import pandas as pd

pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)


orders_data = pd.DataFrame({
    'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10',
                 '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3005, 3001, 3002, 3009, 3005, 3007, 3002, 3004, 3009, 3008, 3003, 3002],
    'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]})


print("Original DataFrame:")
print(orders_data)

print("\nGroup by two columns and count by each row:")
result = orders_data.groupby(['customer_id', 'salesman_id']).size().reset_index().groupby(['salesman_id',
                                                                                           'customer_id'])[[0]].max()

print(result)

# Output:
# Original DataFrame:
#     ord_no  purch_amt    ord_date  customer_id  salesman_id
# 0    70001     150.50  2012-10-05         3005         5002
# 1    70009     270.65  2012-09-10         3001         5005
# 2    70002      65.26  2012-10-05         3002         5001
# 3    70004     110.50  2012-08-17         3009         5003
# 4    70007     948.50  2012-09-10         3005         5002
# 5    70005    2400.60  2012-07-27         3007         5001
# 6    70008    5760.00  2012-09-10         3002         5001
# 7    70010    1983.43  2012-10-10         3004         5006
# 8    70003    2480.40  2012-10-10         3009         5003
# 9    70012     250.45  2012-06-27         3008         5002
# 10   70011      75.29  2012-08-17         3003         5007
# 11   70013    3045.60  2012-04-25         3002         5001
#
# Group by two columns and count by each row:
#                          0
# salesman_id customer_id
# 5001        3002         3
#             3007         1
# 5002        3005         2
#             3008         1
# 5003        3009         2
# 5005        3001         1
# 5006        3004         1
# 5007        3003         1