## Write a Pandas program to select distinct department id from employees file.

import pandas as pd
from bs4 import BeautifulSoup
import requests
import re


url = "https://www.w3resource.com/python-exercises/pandas/sql/departments.php"
response = requests.get(url)
html_content = response.content

if response:
    soup = BeautifulSoup(html_content, "html.parser")
    pre_tag = soup.find("pre", class_="well")
else:
    raise Exception(f"Not able to fetch data due to the following error: {response.status_code}")

ascii_table = pre_tag.text.strip()
lines = ascii_table.split("\n")
lines = [line.strip("| ") for line in lines if not line.startswith("+")]

columns = lines[0].split(" | ")
columns = list(map(lambda x: x.strip(), columns))
columns[-1] = columns[-1].strip().replace(" |", "")
# print(columns)    ['DEPARTMENT_ID', 'DEPARTMENT_NAME', 'MANAGER_ID', 'LOCATION_ID']
rows = [line.split(" | ") for line in lines[1:]]

df = pd.DataFrame(rows, columns=columns)


def clean_cell(cell):
    if isinstance(cell, str):
        return re.sub(r'[\|\r\n]+$', '', cell).strip()
    return cell


# Clean the DataFrame cells
# Also I was getting the following error: DataFrame.applymap has been deprecated, therefore used apply with lambda
df = df.apply(lambda col: col.apply(clean_cell))

# Clean the DataFrame column names
df.columns = [clean_cell(col) for col in df.columns]

csv_file = "departments.csv"
df.to_csv(csv_file, index=False)

print(f'Data successfully written to {csv_file}')
print(df.head(5))

