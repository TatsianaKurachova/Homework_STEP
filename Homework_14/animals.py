     
import sqlite3 as sql

   
data_animals = ((1, 2),
                (2, 4),
                (3, 5),
                (4, 10),
                (5, 10),
                (6, 15),
                (7, 1),
                (8, 3),
                (9, 7),
                (10, 15),)

   
data_male = (('Медведь','мужской', 1),
            ('Кот','мужской', 2),
            ('Ягуар','женский', 3),
            ('Обезьяна','женский', 4),
            ('Лошадь', 'женский', 5),
            ('Собака', 'женский', 6),
            ('Пантера','женский', 7),
            ('Лемур','мужской', 8),
            ('Панда','мужской', 9),
            ('Слон','мужской', 10),)


class Database():
    def __init__(self, data_base):
        self.con = sql.connect(data_base)
        self.cur = self.con.cursor()
        
    def create_animals(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS animals(animal_id INTEGER PRIMARY KEY, age INTEGER)')
        self.con.commit()

    def create_male(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS male(name TEXT, male TEXT, male_id INTEGER)')
        self.con.commit() 
    
    def insert_animals(self, data_animals):
        self.cur.executemany("INSERT INTO animals(animal_id, age) VALUES (?, ?)", data_animals)
        self.con.commit()

    def insert_male(self, data_male):
        self.cur.executemany("INSERT INTO male(name, male, male_id) VALUES (?, ?, ?)", data_male)
        self.con.commit()

    def select(self, query):
        self.cur.execute(f'''{query}''')
        records = self.cur.fetchall()
        return print(records)
   
    def close(self):
        self.con.close()
 
 

database = Database("animals.db")
database.create_animals()
database.create_male()
database.insert_animals(data_animals)
database.insert_male(data_male)
database.select('SELECT name, age FROM animals LEFT JOIN male ON animals.animal_id = male.male_id AND age <= 2')
database.select('SELECT name, age FROM animals INNER JOIN male ON animals.animal_id = male.male_id AND age >= 3')
database.select('SELECT name, male FROM animals INNER JOIN male ON animals.animal_id = male.male_id AND male = "мужской"')



 