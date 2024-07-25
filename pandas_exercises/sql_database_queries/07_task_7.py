# Write a Pandas program to display the first, last name, salary
# and department number for those employees whose first name does not contain the letter 'M'.

import pandas as pd

employees = pd.read_csv('employees.csv')

employees.columns = employees.columns.str.strip().str.lower()

# ~: Negate the boolean Series returned by str.contains to get names that do not contain 'm
filtered_employees = employees[~employees['first_name'].str.contains('m', case=False, na=False)]
result = filtered_employees[['first_name', 'last_name', 'salary', 'department_id']]

print(result)

## or
# print("Last name       First name      Salary    Department ID")
#
# result = employees[employees['first_name'].str.find('M') == -1]
# for index, row in result.iterrows():
#     print(row['last_name'].ljust(15), row['first_name'].ljust(15), str(row['salary']).ljust(9), row['department_id'])


# Equivalent SQL Syntax:
# SELECT FIRST_NAME, LAST_NAME, SALARY, DEPARTMENT_ID
# FROM employees
# WHERE FIRST_NAME NOT LIKE '%M%';