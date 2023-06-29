import requests
#pprint is a package that helps to print json format so it is more readible
import pprint

#Create the variables needed to connect and authenticate. We use the url of the link, we then include a ? to use the parameter
#and we pass the parameter of authentication along with the api key. If we need to pass another parameter we use the ampersand.
#quesiton mark is only used at the beggining. In this case we use the ID as well
url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

parameters = {
        'id':1
    }

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'bb0b0ed9-c02b-4d11-8848-3c71b5ae947d'
}

response = requests.get(url, params=parameters, headers=headers)


print(response.json().get('data', {}).get('1', {}).get('quote', {}).get('USD', {}).get('price', {}))

#pprint.pprint(response.json().get('data').get('1').get('quote').get('USD').get('price'))
