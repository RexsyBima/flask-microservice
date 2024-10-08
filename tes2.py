import requests


from datetime import datetime

time_ = datetime.fromtimestamp(1728398905)
print(time_, type(time_))
print(type(time_.strftime("%Y-%m-%d")))


def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_last_updated_at=true"

    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": "CG-TPkwDzVrwXMqpihXELDY9y23",
    }

    response = requests.get(url, headers=headers)
    json_data = response.json()
    last_updated = datetime.fromtimestamp(json_data["bitcoin"]["last_updated_at"])
    return {
        "status_code": 200,
        "coin": "btc",
        "usd": json_data["bitcoin"]["usd"],
        "last_updated": last_updated,
    }


x = get_btc_price()
print(x)
