import pandas as pd

file = "C:\\Users\\ertan\\Downloads\\data.xlsx"

df = pd.read_excel(file)
# print(df.head(5))
# print(df.dtypes)
# Country, Area, Offered, Handled, Abandoned, Transfers, AHT, Connection Rate

total_offered = df['Offered'].sum()
print(f"Offered: {total_offered}")
total_handled = df['Handled'].sum()
print(f"Handled: {total_handled}")
total_abandoned = df['Abandoned'].sum()
print(f"Abandoned: {total_abandoned}")

# Calculate connection and abandoned rates
connection_rate = round((total_handled / total_offered) * 100, 2)
print(f"Connection Rate: {connection_rate}%")

abandoned_rate = round((total_abandoned / total_offered) * 100, 2)
print(f"Abandoned Rate: {abandoned_rate:.1f}%")

# Convert time strings to timedelta
df['AHT'] = pd.to_timedelta(df['AHT'])
avg_handling_time = df['AHT'].mean()
# Format it to be displayed as follows: HH:MM:SS
format_time = str(avg_handling_time).split()[2][:8]  # ['0', 'days', '00:07:16.857142857']
print(f"Avg Handling Time: {format_time}")

# Output
# Offered: 6277
# Handled: 5749
# Abandoned: 528
# Connection Rate: 91.59%
# Abandoned Rate: 8.4%
# Avg Handling Time: 00:07:16