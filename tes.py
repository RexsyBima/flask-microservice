import requests
from dataclasses import dataclass


@dataclass
class FearAndGreed:
    value: int
    classification: str


url = "https://api.alternative.me/fng/"
resp = requests.get(url).json()
fng = FearAndGreed(
    value=resp["data"][0]["value"],
    classification=resp["data"][0]["value_classification"],
)
print(fng)
