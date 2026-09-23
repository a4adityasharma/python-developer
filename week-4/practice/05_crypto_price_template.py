import requests


def get_price(coin_id="bitcoin", currency="usd"):
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": coin_id,
        "vs_currencies": currency,
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    return data[coin_id][currency]


def main():
    coin = input("Enter CoinGecko coin ID (default: bitcoin): ").strip()
    coin = coin or "bitcoin"

    currency = input("Enter currency (default: usd): ").strip().lower()
    currency = currency or "usd"

    try:
        price = get_price(coin, currency)
        print(f"\n{coin.title()} price: {price} {currency.upper()}")
    except requests.RequestException as error:
        print(f"Network/API error: {error}")
    except (KeyError, TypeError):
        print("Coin or currency was not found in the API response.")


if __name__ == "__main__":
    main()
