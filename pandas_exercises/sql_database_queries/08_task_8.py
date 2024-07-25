# Write a Pandas program to display the first name, last name, salary and
# department number in ascending order by department number.

import pandas as pd

employees = pd.read_csv('employees.csv')

# Note that errors='coerce' will replace any non-numeric values with NaN.
employees['DEPARTMENT_ID'] = pd.to_numeric(employees['DEPARTMENT_ID'], errors='coerce')

# Sort the DataFrame by 'DEPARTMENT_ID' in ascending order with sort_values()
sorted_employees = employees.sort_values(by='DEPARTMENT_ID', ascending=True)

print(sorted_employees[['FIRST_NAME', 'LAST_NAME', 'SALARY', 'DEPARTMENT_ID']])


# Equivalent SQL Syntax:
# SELECT FIRST_NAME, LAST_NAME, SALARY, DEPARTMENT_ID
# FROM employees
# ORDER BY DEPARTMENT_ID;