import os
import pandas as pd
import requests


def fetch_data():
    # Fetch data from the CoinGecko API
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"Not able to fetch data due to an error: {response.status_code}")


def collect_data(current_data):
    # Extract relevant data from JSON
    coins_list = []

    for coin in current_data:
        coins_list.append({
            'name': coin['name'],
            'symbol': coin['symbol'],
            'current_price': round(coin['current_price'], 2),
            'market_cap': coin['market_cap'],
            'total_volume': coin['total_volume']})
    frame = pd.DataFrame(coins_list)
    return frame

# Just added version with map along with lambda
# def collect_data(current_data):
#     # Use map to transform each element of current_data
#     coins_list = list(map(lambda x: {
#         'name': x['name'],
#         'symbol': x['symbol'],
#         'current_price': round(x['current_price'], 2),
#         'market_cap': x['market_cap'],
#         'total_volume': x['total_volume']
#     }, current_data))
#
#     # Convert the list of dictionaries to a DataFrame
#     frame = pd.DataFrame(coins_list)
#     return frame


def load_to_excel_file(data_frame, file_name='crypto_data.xlsx', location='C:\\Users\\Ertan\\Downloads\\'):
    full_path = os.path.join(location, file_name)
    data_frame.to_excel(full_path, index=False)

    return f"File {file_name} has been created successfully"


if __name__ == "__main__":
    # Fetch data from the API
    data = fetch_data()
    # Collect data and create a DataFrame
    df = collect_data(data)
    # Display the DataFrame first five rows
    print(df.head(5))
    print("--------------------------------------------------------------")
    # Save DataFrame to Excel file
    result = load_to_excel_file(df, 'crypto_data.xlsx', 'C:\\Users\\Ertan\\Downloads\\')
    print(result)