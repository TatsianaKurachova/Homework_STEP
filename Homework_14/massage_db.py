     
import sqlite3 as sql

   
data_services = (('Массаж лица', '40 руб'),
                ('Массаж шейно-воротниковой зоны', '30 руб'),
                ('Массаж предплечья', '20 руб'),
                ('Массаж спины', '50 руб'),
                ('Массаж ног', '60 руб'),
                ('Массаж головы', '50 руб'),
                ('Антицеллюлитны массаж', '150 руб'),
                ('Корректирующий массаж', '160 руб'),
                ('Тейпирование спины', '40 руб'),
                ('Тейпирование ягодичных мышц', '50 руб'),)

data_clients = ((1, 'Катя', '+375445558899'),
                (2, 'Маша', '+375296668833'),
                (3, 'Оля', '+375445698214'),
                (4, 'Юля', '+375339996655'),
                (5, 'Андрей', '+375291526897'),
                (6, 'Паша', '+375254568523'),
                (7, 'Дима', '+375448899966'),
                (9, 'Максим', '+375291223366'),
                (10, 'Юра', '+375257779988'),)

    
data_orders = (('001', 1, 'Массаж лица'),
                ('002', 5, 'Массаж шейно-воротниковой зоны'),
                ('003', 7, 'Массаж предплечья'),
                ('004', 10, 'Массаж спины'),
                ('005', 9, 'Массаж ног'),
                ('006', 8, 'Массаж головы'),
                ('007', 6, 'Антицеллюлитны массаж'),
                ('008', 4, 'Корректирующий массаж'),
                ('009', 3, 'Тейпирование спины'),
                ('010', 2, 'Тейпирование ягодичных мышц'),)

class Database():
    def __init__(self, data_base):
        self.con = sql.connect(data_base)
        self.cur = self.con.cursor()
        
    def create_table_client(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS client(client_id INTEGER PRIMARY KEY, client_name TEXT, client_phone TEXT)')
        self.con.commit()
     
    def create_table_services(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS service(service_name TEXT PRIMARY KEY, service_price INTEGER)')
        self.con.commit()

    def create_table_orders(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS orders(orders_id INTEGER PRIMARY KEY, client_id INTEGER, service_name INTEGER, FOREIGN KEY(client_id) REFERENCES client(client_id), FOREIGN KEY(service_name) REFERENCES service(service_name))')
        self.con.commit()
 
    def insert_to_client(self, data_clients):
        self.cur.executemany("INSERT INTO client VALUES (?, ?, ?)", data_clients)
        self.con.commit()
 
    def insert_to_orders(self, data_orders):
        self.cur.executemany("INSERT INTO orders(orders_id, client_id, service_name) VALUES (?, ?, ?)", data_orders)
        self.con.commit()
 
    def insert_to_services(self, data_services):
        self.cur.executemany("INSERT INTO service VALUES (?, ?)", data_services)
        self.con.commit()
 
    def select(self, query):
        self.cur.execute(f'''{query}''')
        records = self.cur.fetchall()
        return print(records)
  
    def close(self):
        self.con.close()
 
 

database = Database("massage_center.db")
database.create_table_services()
database.create_table_client()
database.create_table_orders()
database.insert_to_client(data_clients)
database.insert_to_services(data_services)
database.insert_to_orders(data_orders)
database.select('SELECT * FROM orders')
database.select('SELECT orders_id, client_name, service_name FROM orders INNER JOIN client ON orders.client_id = client.client_id')
 
 