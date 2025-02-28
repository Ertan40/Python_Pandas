import pandas as pd

file = 'C://Users//ertan//Downloads//calls_data_february.xlsx'

df = pd.read_excel(file)
df_cols = df.columns.tolist()

# print(df_cols)
# ['Country', 'Offered Calls', 'Answered Calls', 'Answered Calls %', 'Phone SLA', 'Call Logging', 'Emails Responded',
#  'Email SLA', 'Email Backlog', 'Email Backlog %', 'Offered Chats', 'Answered Chats', 'QA Score']
print(df.dtypes)
print(df.head(5))
# Drop unnecessary columns
df = df.drop(columns=['Offered Chats', 'Answered Chats'])
# print(df.columns.tolist())

# Total offered calls
total_offered_calls = df['Offered Calls'].sum()
print(f"Total offered calls: {total_offered_calls}")

total_answered_calls = df['Answered Calls'].sum()
print(f"Total answered calls: {int(total_answered_calls)}")

# Calculate answered calls percentage
answered_calls_percentage = ((total_answered_calls / total_offered_calls) * 100).round(2).astype('str') + '%'
print(f"Total answered calls %: {answered_calls_percentage}")

total_emails_responded = df['Emails Responded'].sum()
print(f"Total e-mails responded: {total_emails_responded}")

total_email_backlog = df['Email Backlog'].sum()
print(f"Total e-mail backlog: {total_email_backlog}")

# Find answered calls by country level
group_df = df.groupby('Country')['Answered Calls %'].mean().mul(100).round(1).dropna()

# Sort them in descending order
sorted_df = group_df.sort_values(ascending=False).astype('str') + '%'
# Filter for specific countries
countries_to_filter = ['Turkey', 'Bulgaria', 'Portugal', 'Romania', 'Russia']
filtered_df = sorted_df[sorted_df.index.isin(countries_to_filter)]

print(f"\nConnection Rate % by Country Level: {sorted_df}")
print(f"\nConnection Rate % for filtered Countries: {filtered_df}")

# for country, rate in filtered_df.items():
#     print(f"{country}: {rate}%")

# Output:
# Total offered calls: 4557
# Total answered calls: 3967
# Total answered calls %: 87.05%
# Total e-mails responded: 1617
# Total e-mail backlog: 165
#
# Connection Rate % by Country Level: Country
# Israel            96.6%
# Sweden            94.1%
# Romania           93.2%
# Bulgaria          91.3%
# Greece            90.8%
# Ukraine           90.6%
# Portugal          89.1%
# Finland           89.0%
# Russia            88.2%
# Poland            86.9%
# Turkey            86.9%
# Denmark           85.7%
# Hungary           85.1%
# Czech Republic    71.4%
# Slovakia          71.4%
# Norway            50.7%
# Name: Answered Calls %, dtype: object
#
# Connection Rate % for filtered Countries: Country
# Romania     93.2%
# Bulgaria    91.3%
# Portugal    89.1%
# Russia      88.2%
# Turkey      86.9%
# Name: Answered Calls %, dtype: object