import pandas as pd


file_location = 'C:\\Users\\ertan\\Downloads\\voice_august.xlsx'

df = pd.read_excel(file_location)

# print(df.head(5))
# print(df.dtypes)
# Country, Area, Offered, Handled, Abandoned, Transfers, AHT, Connection Rate

avg_connection_rate = df['Connection Rate'].mean()
avg_abandon_rate = df['Abandoned'].mean()
total_offered = df['Offered'].sum()
total_handled = df['Handled'].sum()
# Calculate Abandoned rate
total_abandoned = df['Abandoned'].sum()

abandoned_rate = (total_abandoned / total_offered) * 100
# Convert the 'AHT' column to timedelta
df['AHT'] = pd.to_timedelta(df['AHT'])
avg_handle_time = df['AHT'].mean()
# no_dot = str(avg_handle_time).split('.')[0]  # One of the ways removing after .
avg_time_rounded = avg_handle_time.round('s')   # Second way
total_handle_time = df['AHT'].sum()

print("Please find below overall monthly results:")
print(f"Connection rate: {round(avg_connection_rate, 2) * 100}%")
print(f"Abandoned rate: {round(abandoned_rate, 1)}%")
print(f"Total offered cases: {total_offered}")
print(f"Total handled cases: {round(total_handled)}")
print(f"Total abandoned cases: {round(total_abandoned)}")
print(f"Average handling time: {avg_handle_time}")
print(f"Average handling time: {avg_time_rounded}")
print(f"Total handling time: {total_handle_time}")

# Output:
# Please find below overall monthly results:
# Connection rate: 85.0%
# Abandoned rate: 12.0%
# Total offered cases: 30861
# Total handled cases: 27149
# Total abandoned cases: 3712
# Average handling time: 0 days 00:16:59.551020408
# Average handling time: 0 days 00:17:00
# Total handling time: 0 days 13:52:38
