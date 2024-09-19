import pandas as pd

file = 'C:\\Users\\ertan\\Downloads\\data_raw.xlsx'

df = pd.read_excel(file)

# print(df.head(5))
# print(df.dtypes)

# List of countries to filter
selected_countries = ['Bulgaria', 'Czech Republic', 'Greece', 'Hungary', 'Kazakhstan', 'Poland', 'Romania', 'Russia',
                      'Saudi Arabia', 'Slovakia', 'Turkey', 'Ukraine', 'Utd.Arab Emir.']

# Filter the DataFrame for only the selected countries
filtered_df = df[df['Country'].isin(selected_countries)]
# print(filtered_df)

# Group by 'Country' and count occurrences of 'L4 Problem Code'
problem_code_counts_by_country = filtered_df.groupby('Country')['L4 Problem Code'].size()
# print(pim_counts_by_country)

# Calculate the total number of PIM entries across all selected countries
total_problem_code_count = problem_code_counts_by_country.sum()
print(f"Total problem codes: {total_problem_code_count}")  # 5088

# For PIM count (non-null entries)
pim_counts_by_country = filtered_df.groupby('Country')['PIM'].apply(lambda x: x.notna().sum())
total_pim_counts = pim_counts_by_country.sum()
print("PIM counts by country:")
print(pim_counts_by_country)
print(f"Total PIM counts: {total_pim_counts}")  # 4704

no_pim_counts_by_country = filtered_df.groupby('Country')['PIM'].apply(lambda x: x.isna().sum())
total_no_pim_counts = no_pim_counts_by_country.sum()
# For PIM count (null entries)
print("\nNo PIM counts by country:")
print(no_pim_counts_by_country)
print(f"\nTotal No PIM counts: {total_no_pim_counts}")  # 384

# Let's get top 10 - Products and Top 10 - Drivers
pim_counts = filtered_df.groupby('PIM').size()
sorted_pim_counts = pim_counts.sort_values(ascending=False)
print("Top 10 - Products:")
print(sorted_pim_counts.head(10))

problem_codes_counts = filtered_df.groupby('L4 Problem Code').size()
sorted_problem_codes = problem_codes_counts.sort_values(ascending=False)
print("Top 10 - Drivers:")
print(sorted_problem_codes.head(10))