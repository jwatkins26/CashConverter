from tracemalloc import start
import requests

class Cash_converter:
    rates = {}
    def __init__(self, url):
        data = requests.get(url).json()

        self.rates = data["rates"]

    def converter(self, from_currency, to_currency, amount):
        start_amount = amount
        if from_currency != 'USD':
            amount = amount / self.rates[from_currency]

        amount = round(self.rates[to_currency], 2)
        print(f'{start_amount} {from_currency} = {amount} {to_currency}')


if __name__ == "__main__":
    ACCESS_KEY = '****************'
    url = f'http://data.fixer.io/api/latest?access_key={ACCESS_KEY}'
    c = Cash_converter(url)
    from_country = input('Starting Country >>> ')
    to_country = input('End Country >>> ')
    amount = int(input('Amount >>> '))

    c.converter(from_country, to_country, amount)