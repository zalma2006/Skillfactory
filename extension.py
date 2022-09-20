import requests
import json


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str, keys: dict):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')
        quote_ticker, base_ticker = keys[quote], keys[base]
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Неудалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество')
        r = requests.get(f'https://min-api.cryptocompar'
                         f'e.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[base_ticker]
        return float(total_base)