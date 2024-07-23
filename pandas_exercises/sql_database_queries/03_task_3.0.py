from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

url = "https://www.w3resource.com/python-exercises/pandas/sql/employees.php"
response = requests.get(url)
html_content = response.content

if response:
    soup = BeautifulSoup(html_content, 'html.parser')
    pre_tag = soup.find("pre", class_='well')
else:
    raise Exception(f"Not able to fetch data due to the following error: {response.status_code}")

ascii_table = pre_tag.text.strip()

lines = ascii_table.split('\n')

lines = [line.strip('| ') for line in lines if not line.startswith('+')]

columns = lines[0].split(' | ')
rows = [line.split(' | ') for line in lines[1:]]

df = pd.DataFrame(rows, columns=columns)


# below func is in order to remove trailing pipe character from all columns
def clean_cell(cell):
    return re.sub(r'[\|\r\n]+$', '', cell).strip()


df = df.applymap(clean_cell)
# in order to remove pipe in department_id
df.columns = [clean_cell(col) for col in df.columns]

csv_file = "employees.csv"
df.to_csv(csv_file, index=False)

print(f'Data successfully written to {csv_file}')


