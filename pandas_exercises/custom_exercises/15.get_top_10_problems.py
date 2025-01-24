import pandas as pd

file = "C:\\Users\\ertan\\Downloads\\Problem_Codes_Dec.xlsx"

df = pd.read_excel(file)

print(df.head(5))
print(df.dtypes)

# Filter in order to get only for specific Country
filtered_df = df[df['Country'] == 'Turkey']

# Find the top 10 problems
problem_counts = filtered_df['L4 Problem Code'].value_counts()

# Get the top 10 products
top_ten_problems = problem_counts.head(10)

print(f"Top 10 problems in Turkey: \n{top_ten_problems}")