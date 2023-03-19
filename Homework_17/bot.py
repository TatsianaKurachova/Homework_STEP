import telebot
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import random
from config import TOKEN

engine = create_engine('sqlite:///jokes.db', echo=True)
Base = declarative_base()

bot = telebot.TeleBot(TOKEN)
class Joke(Base):
    __tablename__ = 'jokes'

    id = Column(Integer, primary_key=True)
    text = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
jokes_session = Session()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, " Привет! Я бот который выдает случайные шутки. \n Используй команду /joke для получения случайной шутки. \n Используй команду /add_joke для сохранения шутки.")

@bot.message_handler(commands=['joke'])
def send_joke(message):
    jokes = jokes_session.query(Joke).all()
    joke = random.choice(jokes).text
    bot.send_message(message.chat.id, joke)

@bot.message_handler(commands=['add_joke'])
def add_joke(message):
    joke_text = message.text.split('/add_joke ')[-1]
    joke = Joke(text=joke_text)
    jokes_session.add(joke)
    jokes_session.commit()
    bot.send_message(message.chat.id, "Спасибо. Шутка сохранена!")

bot.polling()