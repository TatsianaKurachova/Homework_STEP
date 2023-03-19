from sqlalchemy.orm import DeclarativeBase, Session, relationship 
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Table, MetaData, Select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# движок
db = 'sqlite:///jokes.db'
engine = create_engine(db, echo=True)
engine.connect()

# базовый класс
class Base(DeclarativeBase):
    pass

# будущая таблица (модель)
class Joke(Base):
    __tablename__ = "jokes"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)

Base.metadata.create_all(bind=engine)

with Session(autoflush=False, bind=engine) as view:
    
   joke1 = Joke(text="Чрезвычайное происшествие: Светская львица задрала фотографов, которые ее снимали")
   joke2 = Joke(text="Одна белка случайно попробовала пиво и поняла зачем она всю жизнь собирала орешки.")
   joke3 = Joke(text="Цистерна - это цилиндр с приваренной к нему дыркой.")
   joke4 = Joke(text="Дагестанские врачи клянутся мамой Гиппократа.")
   joke5 = Joke(text="Хитрые лесорубы раскормили белку-летягу до 120 кг, чтобы самим не валить деревья.")
   joke6 = Joke(text="Как стать гениальным художником? Споткнуться о ведро краски и подождать 100 лет.")
   joke7 = Joke(text="Срочно продаю БМВ. Недорого, 2010 г.в. Не битый, всё есть. Себе бы оставил… но жена сегодня на права сдала, с 7-го раза!")
   joke8 = Joke(text="Я не выговариваю букву 'р' поэтому в моей жизни есть будущее, настоящее и пошлое.")
   joke9 = Joke(text="Очень интересный случай, упасть на лед, а потом им же лечить себе ногу.")
   joke10 = Joke(text="Патриарху хорошо: ему всё можно – подойдёт к зеркалу и прощает себе все грехи.")
   joke11 = Joke(text="С раскрытым ртом слушает свою жену кандидат наук Иван Петрович, чтобы давление на барабанные перепонки снаружи и изнутри было одинаковым.")
   joke12 = Joke(text="Удивительное совпадение - телефон у аспиранта ветеринарного факультета отжали Кабан и Лось.")
   joke13 = Joke(text="Каждый, кто хоть раз собирал мебель из магазина 'Икея', понимает, почему у Швеции нет космической программы.")
   joke14 = Joke(text="Некоторые люди начинаю экономить только когда остаются последние полметра туалетной бумаги.!")
   
   view.add_all([joke1, joke2, joke3, joke4, joke5, joke6, joke7, joke8, joke9, joke10, joke11, joke12, joke13, joke14])
   view.commit() 
 
