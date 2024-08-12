import pandas as pd
import psycopg2
from sqlalchemy import create_engine


df = pd.read_excel("employees_data.xlsx")
# Define Azure PostgreSQL database connection parameters
db_params = {
    "dbname": "demopostgresdb_1",
    "user": "postgresuser",
    "password": "Password1234",
    "host": "demopostgresdb.postgres.database.azure.com",
    "port": "5432"
}

# Create a connection string for SQLAlchemy
connection_string = (f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:"
                     f"{db_params['port']}/{db_params['dbname']}")

try:
    engine = create_engine(connection_string)
    # Upload the DataFrame to PostgreSQL (create table if not exists and append data)
    df.to_sql('employees', engine, if_exists='replace', index=False)
    print("Data has been successfully uploaded to the Azure PostgreSQL database")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Dispose of the SQLAlchemy engine
    if engine:
        engine.dispose()