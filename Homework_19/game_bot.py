import random
import telebot
from config import TOKEN, FOOD_URL

bot = telebot.TeleBot(TOKEN, parse_mode=None)

num = random.randint(1, 100)
chance = 3

@bot.message_handler(commands=['start'])
def start_message(message):
    global num, chance
    num = random.randint(1, 100)
    chance = 3
    bot.reply_to(message, 'Привет!\nДавай сыграем в "угадай число."\nЯ загадал число от 1 до 100!\nУ тебя есть 3 попытки.')

@bot.message_handler(func=lambda message: True)
def game(message):
    global chance, num
    answer = int(message.text.strip())
    if answer == num:
        bot.reply_to(message, f'Ура! Ты угадал {num}!')
        start_message(message)

    elif answer < num:
        chance -= 1
        if chance > 0:
            bot.reply_to(message, f'{answer} меньше, чем мое число! Попробуй ещё раз. У тебя осталось {chance} попыток.')
        else:
            bot.reply_to(message, f'К сожалению, ты не угадал{num}. Попробуй ещё раз.')
            start_message(message)

    elif answer > num:
        chance -= 1
        if chance > 0:
            bot.reply_to(message, f'{answer} больше, чем мое число! Попробуй ещё раз. У тебя осталось {chance} попыток.')
        else:
            bot.reply_to(message, f'К сожалению, ты не угадал число {num}. Попробуй ещё раз')
            start_message(message)


bot.infinity_polling()