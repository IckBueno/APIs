import requests
import pprint

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
parameters = {
    'symbol': 'BTC'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'bb0b0ed9-c02b-4d11-8848-3c71b5ae947d'
}

response = requests.get(url, params=parameters, headers=headers)

if response.status_code == 200:
    data = response.json()

    # Extract the price value
    price = data.get('data', {}).get('BTC', {}).get('quote', {}).get('USD', {}).get('price')

    # Check if the value is a list
    if isinstance(price, list):
        # Access the desired value from the list
        price = price[0].get('price')

    pprint.pprint(price)
else:
    print('Error: Request failed with status code', response.status_code)
