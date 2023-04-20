import requests
# importar instalar requests --> pip install requests

url = 'http://api.weatherapi.com/v1/current.json'
api_key = '<CLAU API>'
params = {
    'key': api_key,
    'q': 'New York City'
}

response = requests.get(url, params=params)

print(response.json())
