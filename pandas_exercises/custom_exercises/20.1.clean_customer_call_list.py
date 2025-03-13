import pandas as pd


file = "C://users//ertan//Downloads//a-datasets//Customer Call List.xlsx"

df = pd.read_excel(file)

print(df.head(5))
print(df.columns.tolist())
# ['CustomerID', 'First_Name', 'Last_Name', 'Phone_Number', 'Address', 'Paying Customer', 'Do_Not_Contact',
#  'Not_Useful_Column']
print(df.isnull().sum())
df = df.drop_duplicates()

df = df.drop(columns='Not_Useful_Column')
# print(df.columns.tolist())
# ['CustomerID', 'First_Name', 'Last_Name', 'Phone_Number', 'Address', 'Paying Customer', 'Do_Not_Contact']

# Clean last_name column
df['Last_Name'] = (
    df['Last_Name'].astype(str)
    .str.replace(r'[/_...]', '', regex=True)
    .str.strip()
)

# Format phone number as follows:  123-545-5421
df['Phone_Number'] = (
    df['Phone_Number'].astype(str)
    # Remove all non-digit characters
    .str.replace(r'[^\d]', '', regex=True)
)
print(df['Phone_Number'])
# Format into XXX-XXX-XXXX
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
# print(df['Phone_Number'])
# We have to clean -- from na vals
df['Phone_Number'] = df['Phone_Number'].str.replace('nan--', '').str.replace('Na--', '').str.replace('--', '')
print(df['Phone_Number'])

df[['Street_Address', 'State', 'Zip_Code']] = df['Address'].str.split(',', n=2, expand=True)
print(df)

# Format Paying Customer column
df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y').str.replace('No', 'N')

# Same apply on 'Do_Not_Contact' however let's use different approach
df['Do_Not_Contact'] = df['Do_Not_Contact'].map({'Yes': 'Y', 'No': 'N'})
print(df['Do_Not_Contact'])
df = df.fillna('')

# Clear clients with 'Y' 'Do_Not_Contact'
for x in df.index:
    if df.loc[x, 'Do_Not_Contact'] == 'Y':
        df.drop(x, inplace=True)

# df = df.dropna(subset='Phone_Number', inplace=True)  # if you want to drop rows with no phone numbers
df = df.reset_index(drop=True)
print(df)