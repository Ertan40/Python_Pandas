# I used Rapid API for this exercise and link is below:
# https://rapidapi.com/rockapis-rockapis-default/api/instant-amazon-data/playground/apiendpoint_697fb51a-1313-4193-9a91-3600f4eb07d1


import requests


def fetch_data_from_api():
    url = 'https://instant-amazon-data.p.rapidapi.com/product-details'
    query_params = {
        'asin': 'B0CM5JV268',
        'country': 'US'
    }
    headers = {
        'x-rapidapi-host': 'instant-amazon-data.p.rapidapi.com',
        'x-rapidapi-key': 'e05082aac1mshd2e48cc18f355f5p144950jsnf5b60481fa02'
    }

    response = requests.get(url, headers=headers, params=query_params)

    # Debugging information
    print(f"Request URL: {response.url}")
    print(f"Request Headers: {response.request.headers}")
    print(f"Response Status Code: {response.status_code}")

    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()


try:
    data = fetch_data_from_api()

    # Extract specific information from the JSON response
    if data.get('success'):
        product_info = data.get('data', {})
        title = product_info.get('title', 'No title available')
        price = product_info.get('price', 'No price available')
        avgStarRating = product_info.get('avgStarRating', 'No rating available')
        product_url = product_info.get('product_url', 'No URL available')
        title_parts = title.split(', ')
        if title:
            print(f"Title: {title_parts[0]}")
        else:
            print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Average Star Rating: {avgStarRating}")
        print(f"Product URL: {product_url}")
        print(f'Tech Specs: {(", ").join(title_parts[1:])}')
        print()
    else:
        print("Failed to fetch product details.")

except Exception as e:
    print(f"An error occurred: {e}")

