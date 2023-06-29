import requests

import pprint

def get_price(id):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

    parameters = {
            'id': id
        }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'bb0b0ed9-c02b-4d11-8848-3c71b5ae947d'
    }

    response = requests.get(url, params=parameters, headers=headers)

    return(response.json().get('data', {}).get(id, {}).get('quote', {}).get('USD', {}).get('price', {}))


response = str(input ("GIVE ME an ID for the price: "))

print(get_price(response))



