## Write a Pandas program to display all the records of REGIONS file.

import pandas as pd


regions = pd.read_csv(r'region.csv')

print(f"All the records from regions file: \n {regions}")



# Equivalent SQL Syntax:
# SELECT * FROM regions;


