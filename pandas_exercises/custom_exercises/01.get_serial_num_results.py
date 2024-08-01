# Unfortunately I can't share the Excel file but idea is to calculate logged serial# for each agent
import pandas as pd


# load the Excel file
df = pd.read_excel('data.xlsx')
# # print(df.head(5))
# below just applied in order to make some checks for individual user
# filtered_df = df[df['Created By'] == '# mmarq186']
# serial_number_count = filtered_df['Serial Number'].count()
# print(f"The number of serial numbers logged by # mmarq186 is: {serial_number_count}")

# Verify data types
print("Data types of columns:")
print(df.dtypes)

total_cases_count = df['Case Number'].count()
no_serial_count = df['Serial Number'].isna().sum()
no_serial = df['Serial Number'].isna()
no_pim_count = df['PIM'].isna().sum()
no_summary_count = df['Summary'].isna().sum()

print(f"No serial count: {no_serial_count}")
print(f"No PIM count: {no_pim_count}")
print(f"No summary count: {no_summary_count}")
print(f"Cases count: {total_cases_count}")
# # # Check unique values in the "Serial Number" column
# # unique_values = df['Serial Number'].unique()
# # print(unique_values)
# Filter DataFrame to include only rows where 'Serial Number' is NaN
missing_serial_df = df[df['Serial Number'].isna()]
# Filter DataFrame to include only rows where 'Serial Number' is not NaN
serial_df = df[df['Serial Number'].notna()]

# Count the number of missing serial numbers per agent
no_serial_count_by_agent = missing_serial_df.groupby('Created By').size()
# Count the number of non-missing serial numbers per agent
serial_count_by_agent = serial_df.groupby('Created By').size()

print("The number of blank serial numbers logged by each agent:")
print(no_serial_count_by_agent)

print("The number of serial numbers logged by each agent:")
print(serial_count_by_agent)

# Calculate percentage of serial numbers logged by each agent
agent_total_counts = df.groupby('Created By').size()
serial_percentage_by_agent = (serial_count_by_agent / agent_total_counts).fillna(0) * 100

# Round percentages to 2 decimal places with percentage sign
serial_percentage_by_agent = serial_percentage_by_agent.round(2).astype(str) + '%'

print("Percentage of serial numbers logged by each agent:")
print(serial_percentage_by_agent)