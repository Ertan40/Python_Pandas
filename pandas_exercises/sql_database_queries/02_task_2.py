## I used web scraping in order to create the "locations.csv" file for the task

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetch the webpage
url = 'https://www.w3resource.com/python-exercises/pandas/sql/locations.php'
response = requests.get(url)
html_content = response.content

# Parse HTML and locate the <pre> tag
soup = BeautifulSoup(html_content, 'html.parser')
pre_tag = soup.find('pre', {'class': 'well'})

# Extract the text content from the <pre> tag
ascii_table = pre_tag.text.strip()

# Split the table into lines
lines = ascii_table.split('\n')

# Remove the borderlines (lines starting with +) and strip each line
lines = [line.strip('| ') for line in lines if not line.startswith('+')]

# Extract column names from the first line
columns = lines[0].split(' | ')

# Extract rows from the remaining lines
rows = [line.split(' | ') for line in lines[1:]]

# Create a DataFrame from the columns and rows
df = pd.DataFrame(rows, columns=columns)

# Write DataFrame to a CSV file
csv_file = 'locations.csv'
df.to_csv(csv_file, index=False)

print(f'Data successfully written to {csv_file}')
