import pandas as pd

file = "C://users//ertan//Downloads//Problem Codes.xlsx"

df = pd.read_excel(file)

print(df.columns.tolist())
print(df.head(5))

# Clean cols
df.columns = [
    col.replace('(Do Not Modify)', '').replace('(Case) (Case)', '').strip()
    for col in df.columns
]

# Filter and find top 5 Country = Turkey
filtered_tr_df = df[df['Country'] == 'Turkey']
product_counts = filtered_tr_df.groupby('Product').size().sort_values(ascending=False)
top5_products_tr = product_counts.head(5)

# Calculate total cases in Turkey (all products)
total_products_tr = product_counts.sum()

# Calculate total top5 products:
total_top5_products_tr = top5_products_tr.sum()

# Calculate percentages for top 5 products
percentages = (top5_products_tr / total_products_tr * 100).round(2)

# Print results
print(f"Top 5 products in Turkey:\n{top5_products_tr}")
print(f"\nTotal top 5 products from Turkey: {total_top5_products_tr}")
print(f"Total products from Turkey: {total_products_tr}")
print(f"\nPercentage by product in Turkey:\n{percentages.astype(str) + '%'}")