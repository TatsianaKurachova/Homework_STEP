# 2) Найдите номер модели, объем памяти и размеры экранов ноутбуков, цена которых превышает 1000 долларов.

from sqlalchemy.orm import DeclarativeBase, Session, relationship 
from sqlalchemy import Column, Integer, String, create_engine, Table, MetaData, Select

# движок
db = 'sqlite:///computer.db'
engine = create_engine(db, echo=True)
engine.connect()

# базовый класс
class Base(DeclarativeBase):
    pass

# будущая таблица (модель)
class Computer(Base):
    __tablename__ = "computers"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String)
    screen_size = Column(Integer)
    speed = Column(String)
    hd = Column(String)
    memory_capacity = Column(String)
    CD = Column(String)
    prise = Column(Integer)


Base.metadata.create_all(bind=engine)

with Session(autoflush=False, bind=engine) as view:
    
    comp_1 = Computer(model = 'Lenovo IdeaPad Gaming 3 15IHU6 (82K101FAPB)', screen_size = 15.6, speed ='3200 МГц', hd = '512 Гб', memory_capacity = '8 ГБ', CD = '12x', prise = 930)
    comp_2 = Computer(model = 'Asus Vivobook 15 X1502ZA-BQ820', screen_size = 15.6, speed ='1500 МГц', hd = '512 Гб', memory_capacity = '8 ГБ', CD = 'Null', prise = 655)
    comp_3 = Computer(model = 'Lenovo IdeaPad 3 15IML05 (81WB0072RE)', screen_size = 15.6, speed ='2400 МГц', hd = '256 Гб', memory_capacity = '4 ГБ', CD = '12x', prise = 450)
    comp_4 = Computer(model = 'Acer Extensa 15 EX215-32-C7HB (NX.EGNEP.00A)', screen_size = 15.6, speed ='1100 МГц', hd = '256 Гб', memory_capacity = '4 ГБ', CD = 'Null', prise = 420)
    comp_5 = Computer(model = 'HP 15s-fq3669nw (584Y6EA)', screen_size = 15.6, speed ='2800 МГц', hd = '256 Гб', memory_capacity = '8 ГБ', CD = 'Null', prise = 430)
    comp_6 = Computer(model = 'Asus ROG Zephyrus Duo 16 GX650RX-LO206W', screen_size = 16, speed ='3300 МГц', hd = '4096 Гб', memory_capacity = '32 ГБ', CD = 'Null', prise = 5823)
    comp_7 = Computer(model = 'MSI Vector GP66 12UHSO-667BY', screen_size = 15.6, speed ='3500 МГц', hd = '1024 Гб', memory_capacity = '32 ГБ', CD = 'Null', prise = 3930)
    comp_8 = Computer(model = 'Моноблок HP ProOne 440 G6 (1C6X9EA)', screen_size = 23.8, speed ='2000 МГц', hd = '256 Гб', memory_capacity = '8 ГБ', CD = '24x', prise = 1382)
    comp_9 = Computer(model = 'Моноблок Z-Tech Office-G64-8-0-240-N-M-000', screen_size = 23.8, speed ='4000 МГц', hd = '240 Гб', memory_capacity = '8 ГБ', CD = 'Null', prise = 528)
    comp_10 = Computer(model = 'Моноблок HP AiO 24 (488J4EA)', screen_size = 23.8, speed ='2400 МГц', hd = '1000 Гб', memory_capacity = '8 ГБ', CD = '24x', prise = 1115)
    comp_11 = Computer(model = 'Apple MacBook Air 13 M2 2022 Silver Z15W0KS ', screen_size = 13.6, speed ='3200 МГц', hd = '256 Гб', memory_capacity = '8 ГБ', CD = 'Null', prise = 1686)
    comp_12 = Computer(model = 'Apple iMac 21,5" Retina 4K MHK33', screen_size = 21.5, speed ='3000 МГц', hd = '256 Гб', memory_capacity = '8 ГБ', CD = 'Null', prise = 2190)
    comp_13 = Computer(model = 'Моноблок Гравитон М52И 107688', screen_size = 23.8, speed ='3300 МГц', hd = '256 Гб', memory_capacity = '8 ГБ', CD = 'Null', prise = 1956)
    comp_14 = Computer(model = 'Моноблок MSI Pro AP241 11M-665RU', screen_size = 23.8, speed ='2500 МГц', hd = '512 Гб', memory_capacity = '16 ГБ', CD = '24x', prise = 1590)
    comp_15 = Computer(model = 'Моноблок Lenovo IdeaCentre 5 24IOB6 F0G3000RRK', screen_size = 23.8, speed ='1300 МГц', hd = '512 Гб', memory_capacity = '8 ГБ', CD = 'Null', prise = 1494)
    comp_16 = Computer(model = 'Apple Macbook Pro 14" M1 Pro 2021 Z15K00079)', screen_size = 14.2, speed ='-', hd = '1024 Гб', memory_capacity = '32 ГБ', CD = 'Null', prise = 9026)
    comp_17 = Computer(model = 'HP Omen 17-ck0045ur 4E1C7EA', screen_size = 17.3, speed ='2300 МГц', hd = '1024 Гб', memory_capacity = '16 ГБ', CD = 'Null', prise = 5351)
    comp_18 = Computer(model = 'MSI Creator Z17 A12UHST-258RU', screen_size = 17.0, speed ='3800 МГц', hd = '2048 Гб', memory_capacity = '64 ГБ', CD = 'Null', prise = 4268)
    comp_19 = Computer(model = 'Digma Eve 14 C414 NA9144BXW01', screen_size = 14.0, speed ='2400 МГц', hd = '128 Гб', memory_capacity = '4 ГБ', CD = 'Null', prise = 250)
    comp_20 = Computer(model = 'ASUS TUF Gaming A15 FA507RE-HN063', screen_size = 15.6, speed ='3200 МГц', hd = '512 Гб', memory_capacity = '8 ГБ', CD = '24x', prise = 1227)
       

   
    q = view.query(Computer.model, Computer.screen_size, Computer.memory_capacity).filter(Computer.prise > 1000).all()
    print(q)