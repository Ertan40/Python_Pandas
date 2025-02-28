import pandas as pd


data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'SalesAmount': [100, 200, 150, 250],
    'Region': ['North', 'South', 'North', 'South']
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Sort by date
df = df.sort_values('Date')

# Calculate cumulative sales
# Overall cumulative
df['Cumulative_Sales'] = df.groupby(df['Date'])['SalesAmount'].transform('sum').cumsum()

# By region cumulative
df['Cumulative_Sales_By_Region'] = df.groupby(['Region', 'Date'])['SalesAmount'].transform('sum').cumsum()