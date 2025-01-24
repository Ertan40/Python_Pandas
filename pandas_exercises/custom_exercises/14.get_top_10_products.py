import pandas as pd
import matplotlib.pyplot as plt

file = "C:\\Users\\ertan\\Downloads\\Problem_Codes_Dec.xlsx"

df = pd.read_excel(file)

print(df.head(5))
print(df.describe())
print(df.dtypes)

# Copy the column
df['Product_cleaned'] = df['Product']

# print(df['Product_cleaned'])
# print(df.head(5))

# Find Top 10 products
product_counts = df['PIM'].value_counts()

# Get the top 10 products
top_10_products = product_counts.head(10)

# Display the top 10 products
print("Top 10 Products:")
print(top_10_products)

# Visualize the top products with matplotlib
top_10_products.plot(kind='bar', title="Top 10 Products")
plt.xlabel("Product")
plt.ylabel("Count")
plt.show()