# Write a Pandas program to display the first name, last name, salary and manager id where manager ids are null.

import pandas as pd

employees = pd.read_csv('employees.csv')

filtered_employees = employees[employees['MANAGER_ID'].isnull()]

result = filtered_employees[['FIRST_NAME', 'LAST_NAME', 'SALARY', 'MANAGER_ID']]
# print(employees.head(5))
print(result)