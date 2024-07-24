## Write a Pandas program to select distinct department id from employees file.

import pandas as pd


employees = pd.read_csv("employees.csv")
departments = pd.read_csv("departments.csv")

print(f"Distinct department_id: \n{employees['DEPARTMENT_ID'].unique()}")

# Equivalent SQL Syntax:
## SELECT DISTINCT DEPARTMENT_ID FROM EMPLOYEES;