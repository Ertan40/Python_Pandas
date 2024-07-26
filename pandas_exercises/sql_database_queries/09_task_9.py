# Write a Pandas program to display the first name, last name, salary
# and department number in descending order by first name.

import pandas as pd

employees = pd.read_csv('employees.csv')

# Sort the DataFrame by 'DEPARTMENT_ID' in ascending order with sort_values()
sorted_employees = employees.sort_values(by='FIRST_NAME', ascending=False)

print(sorted_employees[['FIRST_NAME', 'LAST_NAME', 'SALARY', 'DEPARTMENT_ID']])


# Equivalent SQL Syntax:
# SELECT FIRST_NAME, LAST_NAME, SALARY, DEPARTMENT_ID
# FROM employees
# ORDER BY FIRST_NAME DESC;