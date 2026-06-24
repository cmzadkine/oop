import requests


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