import pandas as pd

file = "C:\\Users\\ertan\\Downloads\\Sales Transaction.csv"


# TransactionNo, Date, ProductNo, ProductName, Price, Quantity, CustomerNo, Country

def clean_data():
    # Load and clean the data
    df = pd.read_csv(file)
    # print(df.head(5))
    # print(df.dtypes)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[df['Quantity'] > 0]
    df['Total_Price'] = df['Price'] * df['Quantity']
    df.to_csv("C:\\Users\\ertan\\Downloads\\Sales_Transaction_cleaned.csv", index=False)
    print("File saved successfully")


def analyze_cleaned_file():
    cleaned_file = "C:\\Users\\ertan\\Downloads\\Sales_Transaction_cleaned.csv"
    df = pd.read_csv(cleaned_file)
    print(df.head(5))
    # Find top 10 the most frequently purchased products
    top_10_products = (df.groupby('ProductName')['Quantity']
                       .sum().sort_values(ascending=False).head(10))
    print('The most frequently purchased 10 products')
    print(top_10_products)


if __name__ == '__main__':
    clean_data()
    analyze_cleaned_file()


