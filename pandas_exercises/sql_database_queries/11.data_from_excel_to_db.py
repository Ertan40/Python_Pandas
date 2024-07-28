## Please note that I didn't add the files due to sensitive information

import pandas as pd
import psycopg2
import openpyxl

df = pd.read_excel('Problem Codes.xlsx')

# Merge the contents of columns 'C' and 'D' into column 'C'
df['Product'] = df['Product'].astype(str) + ' ' + df['Unnamed: 3'].astype(str)

df = df.drop(columns=['Unnamed: 3'])

df.to_excel('cleaned_file.xlsx', index=False)

print("Data cleaned and saved to 'cleaned_file.xlsx'")
cleaned_file = pd.read_excel('cleaned_file.xlsx')
# print(cleaned_file.head(10))
# print(cleaned_file.columns)
# Replace spaces with underscores in column names
# print("Original columns:", cleaned_file.columns)
cleaned_file.columns = cleaned_file.columns.str.replace(' ', '_').str.strip()
# I was getting An error occurred: value too long for type character varying(20), therefore used below check
max_lengths = cleaned_file.map(lambda x: len(str(x))).max()
print(max_lengths)
# cleaned_file['Created On'] = pd.to_datetime(cleaned_file['Created On'])
# print("Cleaned columns:", cleaned_file.columns)
# Establish a connection to the PostgreSQL database
try:
    connection = psycopg2.connect(
        dbname="sales_db",
        user="postgres-user",
        password="password",
        host="127.0.0.1",
        port="5432"
    )
    # Create a cursor object
    cursor = connection.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
             CREATE TABLE IF NOT EXISTS problem_codes (
                 id SERIAL PRIMARY KEY,
                 Case_ID VARCHAR(20),
                 PIM VARCHAR(30),
                 Product VARCHAR(50),
                 L2_Problem_Key_Code VARCHAR(20),
                 L2_Problem_Code VARCHAR(50),
                 L3_Problem_Key_Code VARCHAR(20),
                 L3_Problem_Code VARCHAR(50),
                 L4_Problem_Key_Code VARCHAR(50),
                 L4_Problem_Code VARCHAR(50),
                 L5_Error_Code VARCHAR(120),
                 Remedy_Code VARCHAR(50),
                 Country VARCHAR(50),
                 Created_By VARCHAR(50),
                 Created_On TIMESTAMP
             )
        ''')

    # Insert data from the DataFrame into the PostgreSQL table
    for index, row in cleaned_file.iterrows():
        cursor.execute('''
                    INSERT INTO problem_codes (Case_ID, PIM, Product, L2_Problem_Key_Code, L2_Problem_Code,
                    L3_Problem_Key_Code, L3_Problem_Code, L4_Problem_Key_Code, L4_Problem_Code, L5_Error_Code, 
                    Remedy_Code, Country, Created_By, Created_On)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''', (row['Case_ID'], row['PIM'], row['Product'], row['L2_Problem_Key_Code'], row['L2_Problem_Code'],
                      row['L3_Problem_Key_Code'], row['L3_Problem_Code'], row['L4_Problem_Key_Code'],
                      row['L4_Problem_Code'],
                      row['L5_Error_Code'], row['Remedy_Code'], row['Country'], row['Created_By'], row['Created_On']))

    # Commit the transaction
    connection.commit()

    print("Data imported successfully into the PostgreSQL database.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()

    if connection:
        connection.close()

# print(df.columns)
# Index(['Case ID', 'PIM', 'Product', 'L2 Problem Key Code', 'L2 Problem Code',
#        'L3 Problem Key Code', 'L3 Problem Code', 'L4 Problem Key Code',
#        'L4 Problem Code', 'L5 Error Code', 'Remedy Code', 'Country',
#        'Created By', 'Created On'],
#       dtype='object')

