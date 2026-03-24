import requests

def currency_exchange(currency:str):
    url = "https://open.er-api.com/v6/latest/CHF"

    response = requests.get(url)
    data = response.json()

    # CHF → currency (z.B. CHF → USD)
    rate = data["rates"][currency]

    # Wir brauchen currency → CHF
    return 1 / rate


print(currency_exchange("USD"))