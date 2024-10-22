"""
Exercise 63:

Create a DataFrame and calculate the exponential moving average.
"""

import pandas as pd

# numbers = [i for i in range(1, 7)]
# print(numbers)

data = {'X': [1, 2, 3, 4, 5, 6]}

df = pd.DataFrame(data)

df['Exponential_moving_avg'] = df['X'].ewm(span=3, adjust=False).mean()

print(df)

# Output:
#    X  Exponential_moving_avg
# 0  1                 1.00000
# 1  2                 1.50000
# 2  3                 2.25000
# 3  4                 3.12500
# 4  5                 4.06250
# 5  6                 5.03125
