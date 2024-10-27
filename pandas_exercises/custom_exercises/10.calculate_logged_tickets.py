import pandas as pd

file_location_tickets = 'C:\\Users\\ertan\\Downloads\\call_logging_till_24.10.xlsx'
file_location_calls = 'C:\\Users\\ertan\\Downloads\\calls_by_agent_till_24.10.xlsx'

## Part 1
tickets_df = pd.read_excel(file_location_tickets)
total_cases = tickets_df['Case Number'].count()
total_tickets_df = tickets_df.groupby('Created By').size()
# print(total_tickets_df)

## Part 2 - filter agents and get their calls
calls_df = pd.read_excel(file_location_calls)
agents_to_filter = ['John Doe', 'Jane Smith', 'Michael Johnson', 'Emily Davis', 'Chris Brown', 'Sarah Wilson',
                    'David Lee', 'Laura Martin', 'James Taylor', 'Emma Clark', 'Robert Lewis', 'Olivia Walker',
                    'Daniel Hall']

filtered_calls_df = calls_df[calls_df['Agent Name'].isin(agents_to_filter)]
result = (filtered_calls_df[['Agent Name', 'Answered Calls']]
          .reset_index(drop=True)
          .assign(index=lambda x: x.index + 1)
          .set_index('index')
          .assign(**{'Answered Calls': lambda x: x['Answered Calls'].astype(int)}))

# print(result)

# Part 3 - Convert the Series into a DataFrame and clean the Created By column
total_tickets_df = total_tickets_df.reset_index()
total_tickets_df.columns = ['Created By', 'Tickets']

# Clean the Created By column by removing '#' and any whitespace
total_tickets_df['Created By'] = total_tickets_df['Created By'].str.strip('# ')

# Create a mapping dictionary for user IDs to names
user_id_mapping = {
    'jndoe009': 'John Doe',
    'jmith015': 'Jane Smith',
    'mnson012': 'Michael Johnson',
    'eavis023': 'Emily Davis',
    'crown004': 'Chris Brown',
    'slson004': 'Sarah Wilson',
    'dalee186': 'David Lee',
    'lartin002': 'Laura Martin',
    'jylor002': 'James Taylor',
    'elark003': 'Emma Clark',
    'rewis002': 'Robert Lewis',
    'olker025': 'Olivia Walker',
    'dhall001': 'Daniel Hall'
}

# Add agent names to the tickets DataFrame
total_tickets_df['Agent Name'] = total_tickets_df['Created By'].map(user_id_mapping)

# Merge the DataFrames
merged_df = result.merge(total_tickets_df[['Agent Name', 'Tickets']],
                         on='Agent Name',
                         how='left')

# Reorder columns and reset index
merged_df = (merged_df[['Agent Name', 'Answered Calls', 'Tickets']]
             .reset_index(drop=True)
             .assign(index=lambda x: x.index + 1)
             .set_index('index'))

# print("\nMerged DataFrame:")
# print(merged_df)

# Calculate percentage of logged tickets by agent level
merged_df['Logged Tickets %'] = ((merged_df['Tickets'] / merged_df['Answered Calls']) * 100)
# merged_df['Logged Tickets %'] = ((merged_df['Tickets'] / merged_df['Answered Calls']) * 100).round(2).astype(str) +'%'
sorted_df = merged_df.sort_values(ascending=False, by='Logged Tickets %')
sorted_df['Logged Tickets %'] = sorted_df['Logged Tickets %'].round(2).astype(str) + '%'
reset_index_sorted_df = sorted_df.reset_index(drop=True).assign(index=lambda x: x.index + 1).set_index('index')
print("\nSorted by Logged Tickets DataFrame:")
# print(sorted_df)
print(reset_index_sorted_df)

# Output:
# Sorted by Logged Tickets DataFrame:
#              Agent Name  Answered Calls  Tickets Logged Tickets %
# index
# 1           Chris Brown             102      105          102.94%
# 2          Sarah Wilson             369      360           97.56%
# 3           Emily Davis             127      123           96.85%
# 4       Michael Johnson             331      318           96.07%
# 5          Laura Martin             421      376           89.31%
# 6            Emma Clark             172      149           86.63%
# 7         Olivia Walker             339      280            82.6%
# 8           Daniel Hall             322      231           71.74%
# 9              John Doe             159      114            71.7%
# 10         Robert Lewis             536      353           65.86%
# 11           Jane Smith             395      258           65.32%
# 12         James Taylor              91       46           50.55%
# 13            David Lee             139       53           38.13%