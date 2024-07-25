# Write a Pandas program to display the first and last name,
# and department number for all employees whose last name is "McEwen".

import pandas as pd

employees = pd.read_csv('employees.csv')

print(employees.head(5))
filtered_employees = employees[employees['LAST_NAME'] == 'McEwen']
# print(filtered_employees)
result = filtered_employees[['FIRST_NAME', 'LAST_NAME', 'DEPARTMENT_ID']]
print(result)

### Or via iterrows:
# print("First name  Last name    Department ID")
# result = employees[employees.LAST_NAME == 'McEwen']
# for index, row in result.iterrows():
#     print(row['FIRST_NAME'], '   ', row['LAST_NAME'], '       ', row['DEPARTMENT_ID'])


# Equivalent SQL Syntax:
# SELECT FIRST_NAME, LAST_NAME, DEPARTMENT_ID FROM employees
# WHERE LAST_NAME = "McEwen";