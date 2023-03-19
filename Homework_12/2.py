import sqlite3 as sql

conn = sql.connect('favorites.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS film (
    film_id INTEGER PRIMARY KEY,
    name TEXT,
    year_of_release INT,
    genre TEXT,
    movie_time INT,
    rating INT,
    actors TEXT,
    country TEXT);
    """)

# cur.execute("""INSERT INTO film (film_id, name, year_of_release, genre, movie_time, rating, actors, country)
#         VALUES('001', 'Гарри Поттер и Дары смерти 2 часть', '2011 год', 'Детектив, драма, фэнтази', '130 мин', '4.2/5', 
#                'Дэниэл Рэдклифф, Руперт Гринт, Эмма Уотсон, Хелена Бонем Картер, Робби Колтрейн, Уорвик Дэвис', 
#                'США, Великобритания');""")

# cur.execute("""INSERT INTO film (film_id, name, year_of_release, genre, movie_time, rating, actors, country)
#         VALUES('002', 'Шерлок Холмс', '2009', 'Боевик, триллер, приключения', '128 мин', '3.9/5', 
#                'Роберт Дауни мл., Джуд Лоу, Рэйчел МакАдамс, Марк Стронг, Эдди Марсан, Роберт Мэйллет', 
#                'США, Германия');""")

# cur.execute("""INSERT INTO film (film_id, name, year_of_release, genre, movie_time, rating, actors, country)
#         VALUES('003', 'Плохие парни', '1995', 'Боевик, триллер, комедия', '119 мин', '4/5', 
#                'Уилл Смит, Мартин Лоуренс, Теа Леони, Чеки Карио, Джо Пантольяно, Марг Хельгенбергер', 
#                'США');""")

# cur.execute("""INSERT INTO film (film_id, name, year_of_release, genre, movie_time, rating, actors, country)
#         VALUES('004', 'Шпион по соседству', '2009', 'Боевик, комедия', '94 мин', '4.3/5', 
#                 'Джеки Чан, Эмбер Валлетта, Мадлен Кэрролл, Уилл Шэдли, Алина Фоли, Магнус Шевинг, Билли Рэй Сайрус',
#                'США');""")

cur.execute("SELECT film_id, name, year_of_release, genre, movie_time, rating, actors, country FROM film WHERE year_of_release=2009;")
result = cur.fetchall()
print(result)

conn.commit()