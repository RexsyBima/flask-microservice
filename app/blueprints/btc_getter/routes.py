from datetime import datetime
from app import mail
from flask_mail import Message
import requests
from flask import request
from .bp import btc_getter
import os


@btc_getter.route("/")
def index():
    return "Hello world from btc_getter"


@btc_getter.route("/get_btc", methods=["POST"])
def get_btc():
    email = request.form.get("EMAIL")
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_last_updated_at=true"
    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": os.getenv("COINGECKO_API_KEY"),
    }
    # pay as you use
    request.get_data()
    response = requests.get(url, headers=headers)
    json_data = response.json()
    last_updated = datetime.fromtimestamp(json_data["bitcoin"]["last_updated_at"])
    data = {
        "status_code": 200,
        "coin": "btc",
        "usd": json_data["bitcoin"]["usd"],
        "last_updated": last_updated,
    }
    if email:
        message = Message(
            f"BTC Information - {datetime.now().strftime('%Y-%m-%d')}",
            recipients=[email],
            body=f"""
Hello {email}, here is the current bitcoin price and status
coin name : btc
coin price today is 1 BTC = ${data['usd']}

this price is updated at {data['last_updated']}
            """,
        )
        mail.send(message)
    return data
