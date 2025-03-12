import pandas as pd

file = "C://Users//ertan//Downloads//Problem_Codes_January.xlsx"
output_file = "C://Users//ertan//Downloads//Russia_Analysis.xlsx"  # Output file path

df = pd.read_excel(file)
# df_cols = df.columns.tolist()
# print(df.head(5))
# print(df_cols)

# Drop the unnecessary column
df = df.drop(columns='Unnamed: 3')
df_cols = df.columns.tolist()

# Filter to get desired Country
filtered_df = df[df['Country'] == 'Russia']

# Get top products and problems
top_products = filtered_df.groupby('PIM').size().sort_values(ascending=False).head(5)
print('Top 5 products in Russia:')
print(top_products)

top_problems = filtered_df.groupby('L4 Problem Code').size().sort_values(ascending=False).head(5)
print('\nTop 5 problems in Russia:')
print(top_problems)

# Save into Excel file
# Convert Series to DataFrames for better Excel formatting
top_products_df = top_products.reset_index(name='Count')
top_problems_df = top_problems.reset_index(name='Count')

# Save to Excel with multiple sheets
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    top_products_df.to_excel(writer, sheet_name='Top_Products', index=False)
    top_problems_df.to_excel(writer, sheet_name='Top_Problems', index=False)


print(f'Results saved to {output_file}')