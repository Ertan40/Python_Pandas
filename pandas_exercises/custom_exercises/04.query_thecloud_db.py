import pandas as pd
from sqlalchemy import create_engine

# Define Azure PostgreSQL database connection parameters
db_params = {
    "dbname": "demopostgresdb_1",
    "user": "postgresuser",
    "password": "Password1234",
    "host": "demopostgresdb.postgres.database.azure.com",
    "port": "5432"
}

# Create a connection string for SQLAlchemy
connection_string = (f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}"
                     f"/{db_params['dbname']}")

# Establish the connection and query the data
try:
    engine = create_engine(connection_string)
    # Query the table
    df = pd.read_sql('SELECT * FROM employees LIMIT 10', engine)
    print(df)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Dispose of the SQLAlchemy engine
    if engine:
        engine.dispose()


## Output which confirms that we had a successful implementation
#    id first_name   last_name  ... department_id manager_id address_id
# 0   5    Thierry      D`Hers  ...             5         19         40
# 1   6      David     Bradley  ...             5        109        199
# 2   7       Ruth  Ellerbrock  ...             7        185        108
# 3   8       Gail    Erickson  ...             1          3         22
# 4   9      Barry     Johnson  ...             7        185        285
# 5  10     Jossef    Goldberg  ...             1          3        214
# 6  11      Terri       Duffy  ...             1        109        209
# 7  12     Sidney        Higa  ...             7        185         73
# 8  13     Taylor     Maxwell  ...             7         21         82
# 9  14    Jeffrey        Ford  ...             7        185        156
#
# [10 rows x 10 columns]
# it might be checked through psql as well
# psql ("host=demopostgresdb.postgres.database.azure.com port=5432 dbname=demopostgresdb_1 user=postgresuser "
#       "password=Password1234 sslmode=require")

