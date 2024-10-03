from .bp import fng_bp
from app import mail
from flask_mail import Message

import requests
from datetime import datetime
from dataclasses import dataclass


@dataclass
class FearAndGreed:
    value: int
    classification: str


@fng_bp.route("/")
def index():
    return "Hello world from fng bp"


@fng_bp.route("/get_fng/<email>")
def get_fng(email):
    resp = requests.get("https://api.alternative.me/fng/").json()
    fng = FearAndGreed(
        value=resp["data"][0]["value"],
        classification=resp["data"][0]["value_classification"],
    )
    date = datetime.now().strftime("%Y-%m-%d")
    message = Message(
        subject=f"Fear and Greed - date {date} - classification {fng.classification}",
        recipients=[email],
        body=f"Today's fear and greed {date} is at value {fng.value} with classification {fng.classification} \n\n source : https://api.alternative.me/fng/",
    )
    mail.send(message)
    return {"status_code": 200}
