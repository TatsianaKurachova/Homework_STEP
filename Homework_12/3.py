import sqlite3 as sql

conn = sql.connect('favorites.db')
cur = conn.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS technic (
#     technic_id INTEGER PRIMARY KEY,
#     name TEXT,
#     price INT,
#     company TEXT,
#     model TEXT,
#     color TEXT,
#     country_of_origin TEXT,
#     energy_consumption_class TEXT);
#      """)

# cur.execute("""INSERT INTO technic (technic_id, name, price, company, model, color, country_of_origin, energy_consumption_class)
#         VALUES('001', 'Робот-пылесос', '1369', 'Xiaomi', 'Mi Robot Vacuum S10T BHR5887EU/STFCR01SZ', 'белый', 'Китай', '');""")

# cur.execute("""INSERT INTO technic (technic_id, name, price, company, model, color, country_of_origin, energy_consumption_class)
#         VALUES('002', 'Посудомоечная машина', '3209', 'Electrolux', 'KECB8300L', 'белый', 'Польша', 'A+++');""")

# cur.execute("""INSERT INTO technic (technic_id, name, price, company, model, color, country_of_origin, energy_consumption_class)
#         VALUES('003', 'Кофемашина', '4205.3', 'DeLonghi', 'DeLonghi', 'черный, серебристый', 'Китай', '');""")

# cur.execute("""INSERT INTO technic (technic_id, name, price, company, model, color, country_of_origin, energy_consumption_class)
#         VALUES('004', 'Плойка', '679', 'Philips', 'BHB876/00', 'черныц', 'Китай', '');""")

cur.execute("SELECT technic_id, name, price, company, model, color, country_of_origin, energy_consumption_class FROM technic WHERE price < 1200;")
result = cur.fetchall()
print(result)

conn.commit()