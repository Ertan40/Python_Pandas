"""
27. Write a Pandas program to split a given dataset, group by one column and apply an aggregate function
to few columns and another aggregate function to the rest of the columns of the dataframe.
"""

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.DataFrame({
    'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001],
    'sale_jan': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 1760, 2983.43, 480.4, 1250.45, 75.29, 1045.6],
    'sale_feb': [250.5, 170.65, 15.26, 110.5, 598.5, 1400.6, 2760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'sale_mar': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'sale_apr': [150.5, 270.65, 95.26, 210.5, 948.5, 2400.6, 760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'sale_may': [130.5, 270.65, 65.26, 310.5, 948.5, 2400.6, 760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'sale_jun': [150.5, 270.65, 45.26, 110.5, 948.5, 3400.6, 5760, 983.43, 2480.4, 250.45, 75.29, 3045.6],
    'sale_jul': [950.5, 270.65, 65.26, 210.5, 948.5, 2400.6, 5760, 983.43, 2480.4, 250.45, 75.29, 3045.6],
    'sale_aug': [150.5, 70.65, 65.26, 110.5, 948.5, 400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'sale_sep': [150.5, 270.65, 65.26, 110.5, 948.5, 200.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'sale_oct': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'sale_nov': [150.5, 270.65, 95.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'sale_dec': [150.5, 70.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6]
})
print("Original Orders DataFrame:")
print(df)

grouped_df = df.groupby(
    'salesman_id').agg(lambda x: x.sum() if x.name in ['sale_jan', 'sale_feb', 'sale_mar'] else x.mean()
                       )

print("\nResult after group on salesman_id and apply different aggregate functions:")
print(grouped_df)
