import requests
from dataclasses import dataclass


@dataclass
class CryptoPrijs:
    naam: str
    prijs_eur: float

    def toon(self):
        print(f"{self.naam}: €{self.prijs_eur:.2f}")


class ApiClient:
    URL = "https://api.coingecko.com/api/v3/simple/price"

    def fetch_price(self, coin="bitcoin"):
        params = {
            "ids": coin,
            "vs_currencies": "eur"
        }

        response = requests.get(self.URL, params=params, timeout=5)
        response.raise_for_status()
        return response.json()


def parse_crypto(data, coin="bitcoin"):
    prijs = data[coin]["eur"]
    return CryptoPrijs(coin.capitalize(), prijs)