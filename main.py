import requests

url = 'https://api.oilpriceapi.com/v1/prices/latest'
headers = {
    'Authorization': 'Token b7ed054ba6e6d513af611db4e0b0e7f2',
    'Content-Type': 'application/json'
}

response = requests.get(url=url, headers=headers)
data = response.json()
print(data)
