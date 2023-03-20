import requests
import telebot
from config import TOKEN, FOOD_URL

bot = telebot.TeleBot(TOKEN, parse_mode=None)
url_food = FOOD_URL

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm a food bot. \nIf you want to get information about new food, enter /food")


@bot.message_handler(commands=['food'])
def send_food(message):
    response = requests.get(url_food)
    data = response.json()['meals'][0]
    food_name = data['strMeal'] 
    picter_food = data['strMealThumb']
    category_food = data['strCategory']
    ingredients = [] 
    for i in range(1, 20):
        if data[f'strIngredient{i}'] != "":
            ingredient = data[f'strMeasure{i}'].strip() + " " + data[f'strIngredient{i}'].strip() 
            ingredients.append(ingredient)
    recipe = data['strInstructions'] 
    response_message = f"<b>{food_name}</b>\n{category_food}\n{picter_food}\nИнгредиенты:\n"
    for ingredient in ingredients:
        response_message += f"- {ingredient}\n"
    response_message += f"\nПриготовление:\n{recipe}"
    bot.send_message(message.chat.id, response_message, parse_mode='HTML')


bot.infinity_polling()