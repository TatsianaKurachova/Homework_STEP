import sqlite3 as sql
from sqlite3 import Error

def sql_connection():
    try:
        con = sql.connect('shop.db')
        return con
    except Error:
        print (Error)
    
def sql_table(con):
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (book_id integer PRIMARY KEY, title_of_the_book text, author text, year_of_publication int, publishing_house text)")
    con.commit()

# def sql_insert(con, data):
#     cur = con.cursor()
#     cur.executemany("INSERT INTO book (book_id, title_of_the_book, author, year_of_publication, publishing_house) VALUES(?, ?, ?, ?, ?)", data)
#     con.commit()

def sql_fetchall(con):
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    for row in rows:
        print (row)
    con.commit()

# data = ((1, 'Гарри Поттер и узник Азкабана', 'Джуана Роулинг', 2009, 'РОСМЕН'),
#         (2, 'Зеленая Миля', 'Стивинг Кинг', 2014, 'АСТ'),
#         (3, 'Унесенные ветром', 'Маргарет Митчелл', 2020, 'Азбука-Атикус'),
#         (4, 'Шерлок Холмс', 'Артур Конан Дойл', 2019, 'Алгоритм'),
#         (5, 'Гарри Поттер и Принц Полукровка', 'Джуана Роулинг', 2005, 'РОСМЕН'),
#         (6, 'Граф Монтекристо', 'Александр Дюма', 2017, 'Азбука-Атикус'),
#         (7, 'Тайная Опара. Привязанность в жизни ребенка', 'Людмила Петрановская', 2016, 'АСТ'),
#         (8, 'Побег из Шоушенга', 'Стивин Кинг', 2011, 'Астрель'),
#         (9, 'Мастер и Маргарита', 'Михаил Булгаков', 2006, 'Вече'),
#         (10, 'Записки о Шерлоке Холмсе', 'Артур Конан Дойл', 2015, 'Азбука-Атикус'),)

def extract_all_of_id(con):
    cur = con.cursor()
    cur.execute("SELECT book_id, title_of_the_book, author, year_of_publication, publishing_house FROM book WHERE book_id =5")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    con.commit()

con = sql_connection()
# sql_table(con)
# sql_insert(con, data)
# sql_fetchall(con)
extract_all_of_id(con)

