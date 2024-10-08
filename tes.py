import requests

url = "https://api.coingecko.com/api/v3/simple/price"
API_KEY = "CG-TPkwDzVrwXMqpihXELDY9y23"
headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": API_KEY,
}
resp = requests.get(url, headers=headers)
print(resp.text)
