# Write a Pandas program to display the first, last name, salary and
# department number for those employees whose first name starts with the letter 'S'.


import pandas as pd

employees = pd.read_csv('employees.csv')

# Normalize the column names to ensure consistency (if needed)
# employees.columns = employees.columns.str.strip().str.upper()

# filtered_employees = employees[employees['FIRST_NAME'].str.startswith('S')]
# result = filtered_employees[['FIRST_NAME', 'LAST_NAME', 'SALARY', 'DEPARTMENT_ID']]
#
# # print(filtered_employees)
# print(result)

# second solution:
print("First name       Last name      Salary    Department ID")
result = employees[employees['FIRST_NAME'].str[:1] == 'S']
for index, row in result.iterrows():
    print(row['FIRST_NAME'].ljust(15), row['LAST_NAME'].ljust(15), str(row['SALARY']).ljust(9), row['DEPARTMENT_ID'])


# Equivalent SQL Syntax:
# SELECT FIRST_NAME, LAST_NAME, SALARY, DEPARTMENT_ID
# FROM employees
# WHERE FIRST_NAME LIKE 'S%';