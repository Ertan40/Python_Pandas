## Write a Pandas program to extract first 7 records from employees file.


import pandas as pd


employees = pd.read_csv("employees.csv")

print(f"Extract first 7 records from employees file: \n{employees.head(7)}")

# Equivalent SQL Syntax:
# SELECT * FROM employees
# LIMIT 7;