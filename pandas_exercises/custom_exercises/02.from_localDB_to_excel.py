import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# install libraries if you haven't yet: pip install pandas psycopg2-binary sqlalchemy openpyxl
# Define the database connection parameters

db_params = {
    "dbname": "sqldemos_db",
    "user": "postgres-user",
    "password": "password",
    "host": "127.0.0.1",
    "port": "5432"
}

# Create a connection string for SQLAlchemy
connection_string = (f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:"
                     f"{db_params['port']}/{db_params['dbname']}")

# Establish connection
try:
    engine = create_engine(connection_string)
    # Use pandas to read data
    query = "SELECT * FROM employees"
    df = pd.read_sql(query, engine)

    # Write the DataFrame to an Excel file
    df.to_excel("employees_data.xlsx", index=False)
    print("Data has been successfully written to employees_data.xlsx")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if engine:
        engine.dispose()

# Check whether data is OK
# read_new_file = pd.read_excel("employees_data.xlsx")
# print(read_new_file.head(10))



