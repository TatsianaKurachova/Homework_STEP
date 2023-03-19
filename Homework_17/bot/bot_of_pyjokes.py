import requests
import random
import pyjokes
from config import TOKEN, BASE_URL

def updates():
    current_updates_link = BASE_URL + 'getupdates'
    request = requests.get(current_updates_link)
    return request.json()

def message():
    data = updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    last_message = data['result'][-1]['message']['text']
    message_list = {'chat_id': chat_id, 'text': last_message}
    return message_list

def send_message(chat_id, text='...'):
    url = BASE_URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)  


def bot_joke():
    joke = message()
    text = joke['text']
    id = joke['chat_id']

    if text == '/joke':
        My_joke = pyjokes.get_joke(language="en", category="neutral")
        send_message(id, My_joke)

bot_joke()

