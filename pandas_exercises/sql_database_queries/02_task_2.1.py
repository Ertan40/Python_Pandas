## Write a Pandas program to display all the location id from locations file.


import pandas as pd

df = pd.read_csv("locations.csv")
result = df[["LOCATION_ID"]]

print(f"All the locations id from locations file: {result}")

# Equivalent SQL Syntax:
# SELECT LOCATION_ID FROM locations;