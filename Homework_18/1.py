import requests
import telebot
from config import TOKEN, BANK_URL, DOG_URL

bot = telebot.TeleBot(TOKEN, parse_mode=None)
url = BANK_URL
url_dog = DOG_URL

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm a crypto and dog bot. \nIf you want to get information about crypto currency, enter /crypto\nIf you want to get a picture with a dog, enter /dog")

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

@bot.message_handler(commands=['dog'])
def get_dog(message):
    response = requests.get(url_dog)
    image_url = response.json()['message']
    bot.send_photo(message.chat.id, image_url)


bot.infinity_polling()