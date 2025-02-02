"""
Write a Pandas program to split a given dataframe into groups with bin counts.
Test Data:
    ord_no  purch_amt  customer_id  sales_id
0    70001     150.50         3005      5002
1    70009     270.65         3001      5003
2    70002      65.26         3002      5004
3    70004     110.50         3009      5003
4    70007     948.50         3005      5002
5    70005    2400.60         3007      5001
6    70008    5760.00         3002      5005
7    70010    1983.43         3004      5007
8    70003    2480.40         3009      5008
9    70012     250.45         3008      5004
10   70011      75.29         3003      5005
11   70013    3045.60         3002      5001
"""
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.DataFrame({
    'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'customer_id': [3005, 3001, 3002, 3009, 3005, 3007, 3002, 3004, 3009, 3008, 3003, 3002],
    'sales_id': [5002, 5003, 5004, 5003, 5002, 5001, 5005, 5007, 5008, 5004, 5005, 5001]})

print("Original DataFrame:")
print(df)

groups = df.groupby(["customer_id", pd.cut(df.sales_id, 3)], observed=False)
result = groups.size().unstack()
print(result)

# Output:
# Original DataFrame:
#     ord_no  purch_amt  customer_id  sales_id
# 0    70001     150.50         3005      5002
# 1    70009     270.65         3001      5003
# 2    70002      65.26         3002      5004
# 3    70004     110.50         3009      5003
# 4    70007     948.50         3005      5002
# 5    70005    2400.60         3007      5001
# 6    70008    5760.00         3002      5005
# 7    70010    1983.43         3004      5007
# 8    70003    2480.40         3009      5008
# 9    70012     250.45         3008      5004
# 10   70011      75.29         3003      5005
# 11   70013    3045.60         3002      5001
# sales_id     (5000.993, 5003.333]  (5003.333, 5005.667]  (5005.667, 5008.0]
# customer_id
# 3001                            1                     0                   0
# 3002                            1                     2                   0
# 3003                            0                     1                   0
# 3004                            0                     0                   1
# 3005                            2                     0                   0
# 3007                            1                     0                   0
# 3008                            0                     1                   0
# 3009                            1                     0                   1
