"""
Exercise 62:

Create a DataFrame with datetime index and resample by month
"""

import pandas
import pandas as pd

data_range = pd.date_range(start='1/1/2024', periods=100, freq='D')

data = {'X': range(100)}

df = pd.DataFrame(data, index=data_range)

monthly_df = df.resample('ME').sum()

print(monthly_df)

# output
#                X
# 2024-01-31   465
# 2024-02-29  1305
# 2024-03-31  2325
# 2024-04-30   855