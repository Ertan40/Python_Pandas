## Write a Pandas program to compare the elements of the two Pandas Series.
## Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]

import pandas as pd


numbers = list(range(1, 11))
numbers_1 = [num for num in numbers if num % 2 == 0]
numbers_2 = list(filter(lambda x: x % 2 != 0 and x < 9, numbers))
numbers_2.append(10)

ds1 = pd.Series(numbers_1)
ds2 = pd.Series(numbers_2)

print(f"Series1: \n{ds1}")
print(f"Series2: \n{ds2}")
print("Compare the elements of the said Series:")
print(f"Equals: \n{ds1==ds2}")
print(f"Greater than: \n{ds1 > ds2}")
print(f"Less than: \n{ds1 < ds2}")