import sqlite3 as sql

conn = sql.connect('favorites.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS food (
    food_id INTEGER PRIMARY KEY,
    name TEXT,
    protein INT,
    fast INT,
    carbohydrate INT,
    calories INT,
    ingredients TEXT,
    recipe TEXT);
    """)

cur.execute("""INSERT INTO food (food_id, name, protein, fast, carbohydrate, calories, ingredients, recipe)
        VALUES('001', 'Омлет с помидором', '33.93', '24.5', '14.09', '408', 
               'молоко - 120г, яйцо - 1шт , сыр - 35г, помидор - 1шт', 
               'Яйцо взбить с молоком, добавить соль. Нарезать помидор. Натереть сыр. Все перемешать. Обжарить на сковородке');""")

cur.execute("""INSERT INTO food (food_id, name, protein, fast, carbohydrate, calories, ingredients, recipe)
        VALUES('002', 'Запеченая груша с творогом', '15.59', '1.56', '18.6', '147', 
               'груша - 145г, творог - 120г', 
               'Разрезать грушу пополам, почистить от семечек. Выложить творожную шапку. Запекать 25-30 мин на 180 градусах');""")

cur.execute("""INSERT INTO food (food_id, name, protein, fast, carbohydrate, calories, ingredients, recipe)
        VALUES('003', 'Тушеная говядина с овощным салатом', '24.33', '30.06', '14.43', '420', 
               'говядина - 220г, сладкий перец - 90г, салат айсберг - 60г, огурец - 30г, помидор - 60г, оливковое масло, лимонный сок, кунжут', 
               'Говодину нарезать брусками, потушить около 60 минут до готовности. Нарезать и смешать овощи. Заправить лимонно-масляной заправкой');""")

cur.execute("""INSERT INTO food (food_id, name, protein, fast, carbohydrate, calories, ingredients, recipe)
        VALUES('004', 'Яблочно черничный рулет', '29.03', '9.42', '60.06', '436', 
               'черника - 30г, тонкий лаваш - 60г, творог - 120г, яйцо - 1шт, яблоко - 60г', 
               'Отделить яичный белок от жельтка. Взбить творог с яичным белком. Смазать лаваш творожной смесью. Разложить нарезанные яблоки и чернику, завернуть. 
                Смазать яичным желтком и поставить в разогретую до 180 градусов духовку на 25-30минут');""")

conn.commit()

