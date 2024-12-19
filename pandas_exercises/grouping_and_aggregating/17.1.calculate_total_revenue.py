"""
Raw Transactional Data:
TransactionID	CustomerID	TransactionDate	Amount	Region
1	101	2023-11-01	100	East
2	102	2023-11-01	200	West
3	101	2023-11-02	150	East
4	103	2023-11-02	300	South
Report Requirement:
Total revenue by region for each day.
Include only regions with total daily revenue greater than $200.
"""

import pandas as pd

data = {"TransactionID": [1, 2, 3, 4], "CustomerID": [101, 102, 103, 104],
        "TransactionDate": ["2023-11-01", "2023-11-01", "2023-11-02", "2023-11-02"],
        "Amount": [100, 200, 150, 300], "Region": ["East", "West", "East", "South"]}


df = pd.DataFrame(data)
# Group by TransactionDate and Region, sum the Amount
result = df.groupby(['TransactionDate', 'Region'])["Amount"].sum().reset_index()\
        .rename(columns={"Amount": "Total_Revenue"})
# # Filter for regions with daily revenue > 200
result = result[result["Total_Revenue"] > 200]
result["Total_Revenue"] = result["Total_Revenue"].apply(lambda x: f"${x:.2f}")
print(result)
# Output:
# TransactionDate Region Total_Revenue
# 3      2023-11-02  South       $300.00
