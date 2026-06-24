from models.crypto import CryptoPrijs


def parse_crypto(data, coin="bitcoin"):
    prijs = data[coin]["eur"]
    return CryptoPrijs(coin.capitalize(), prijs)