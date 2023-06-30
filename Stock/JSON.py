import requests


url = 'https://eodhistoricaldata.com/api/eod/BMO.US?fmt=json&from=2010-01-01&to2023-06-01&api_token=649dc4aeecaf08.01206507'
response = requests.get(url)


print(response.json())
#pprint.pprint(response.json())