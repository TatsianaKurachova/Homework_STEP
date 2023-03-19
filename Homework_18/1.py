import requests
import telebot
from config import TOKEN, BANK_URL

bot = telebot.TeleBot(TOKEN, parse_mode=None)
url = BANK_URL

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm a crypto bot to output the top-5 crypto currencies, enter the command /crypto")

@bot.message_handler(commands=['crypto'])
def get_crypto_info(message):
    response = requests.get(url).json()
    crypto_data = ''
    for data in response[:5]:  
        symbol = data['symbol']
        last_price = data['lastPrice']
        price_change_percent = data['priceChangePercent']
        crypto_data += f'\n{symbol}: {last_price} ({price_change_percent}%)'
    bot.send_message(message.chat.id, crypto_data)

bot.infinity_polling()