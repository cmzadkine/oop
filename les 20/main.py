from api_client import ApiClient, parse_crypto


def main():
    client = ApiClient()

    data = client.fetch_price("bitcoin")
    crypto = parse_crypto(data)

    crypto.toon()


if __name__ == "__main__":
    main()