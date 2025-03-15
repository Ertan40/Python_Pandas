import pandas as pd
from sqlalchemy import create_engine

# File paths
products = "C://users//ertan//Downloads//a-datasets//powerBI_project//Products.csv"
sales = "C://users//ertan//Downloads//a-datasets//powerBI_project//SalesData.csv"
stores = "C://users//ertan//Downloads//a-datasets//powerBI_project//Stores.csv"

# Load data
df_products = pd.read_csv(products)
df_sales = pd.read_csv(sales)
df_stores = pd.read_csv(stores)

# Database connection parameters
db_params = {
    'dbname': 'your_dbname',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'port': 'your_port'
}

# Create connection string
connection_string = (f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:"
                     f"{db_params['port']}/{db_params['dbname']}")

# Initialize engine outside the try block to ensure it's accessible in finally
engine = None

try:
    engine = create_engine(connection_string)

    # Write DataFrames to PostgreSQL
    df_products.to_sql('products', con=engine, if_exists='append', index=False)
    df_sales.to_sql('sales', con=engine, if_exists='append', index=False)
    df_stores.to_sql('stores', con=engine, if_exists='append', index=False)

    print("All tables have been successfully written to the database.")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    if engine:
        engine.dispose()
        print("Database connection closed.")