import re
import telebot

path = r'/media/maks/общее/Максим/Обучение_skillfdsfactory/PassBot.txt'


def token_stock(path: str) -> str:
    try:
        with open(path, 'r') as f:
            line = f.read().split('\n')
            line = [x for x in line if x != '']
            tokens = {re.split('=', i)[1]: re.split('=', i)[0] for i in line}
        return tokens
    except FileNotFoundError:
        print('Файл не найден, значение ключа взято по умолчанию')
        tokens = {'StockChangeBot': ''} # в значение ввести ТОКЕН
        return tokens


def telebot_f(token):
    return telebot.TeleBot(token)


tokens_bots = token_stock(path)
TOKEN = tokens_bots['StockChangeBot']

bot = telebot_f(TOKEN)

keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'}
