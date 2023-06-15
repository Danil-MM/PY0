import sqlite3

connection = sqlite3.connect("db.db")
cursor = connection.cursor()

cursor.execute('''  CREATE TABLE if not exists Seller(
id INTEGER PRIMARY KEY AUTOINCREMENT,
NAME TEXT,
ProductName TEXT,
ProductPrice INT)''')

cursor.execute(''' create table if NOT EXISTS PVZ(
id INTEGER PRIMARY KEY AUTOINCREMENT,
city text,
street text
)''')

cursor.execute('''create table if NOT EXISTS Buyer(
id integer PRIMARY KEY AUTOINCREMENT,
FirstName text,
SecondName text
)  ''')

cursor.execute(''' create table if not exists TakeOrder(
order_id integer PRIMARY KEY AUTOINCREMENT,
seller_id INTEGER not null,
buyer_id INTEGER NOT NULL,
PVZ_id INTEGER NOT NULL,
status text DEFAULT 'Не выдано',
foreign key (PVZ_id) references PVZ(id),
foreign key (buyer_id) references buyer(id),
foreign key (seller_id) references seller(id)
);''')


SellerName = [
    ('ИП_Электрик','Лампа светодиодная', 300),
    ('ИП_Электрик', 'Розетка евро', 199),
    ('ИП_Электрик', 'Люстра ЛЮКС', 6690),
    ('ДНС', 'Клавиатура', 3490),
    ('Мир_Техники', 'Цветной МФУ', 12990),
    ('ЯСтроитель','Газонокосилка бензиновая', 19990)
]

cursor.executemany(''' INSERT INTO Seller(Name,ProductName,ProductPrice)
                        VALUES (?,?,?) 
                        ''', SellerName)

PVZ= [('Москва', 'Пушкина,89'),
      ('Пермь', 'Попова,42А'),
      ('Саратов', 'Мельникова, 12')]

cursor.executemany(''' INSERT INTO PVZ(city,street)
                        VALUES (?,?) 
                        ''', PVZ)

buyer=[('Сергей','Сергеев'),
       ('Никита','Михайлов'),
       ('Валерия', 'Смолина'),
       ('Семён','Малинин')]


cursor.executemany(''' INSERT INTO Buyer(FirstName,SecondName)
                        VALUES (?,?) 
                        ''', buyer)

cursor.execute(''' insert into TakeOrder (seller_id, PVZ_id, buyer_id) values ( 2, 1, 1); ''')
cursor.execute(''' insert into TakeOrder (seller_id, PVZ_id, buyer_id) values ( 3, 2, 4); ''')
cursor.execute(''' insert into TakeOrder (seller_id, PVZ_id, buyer_id) values ( 1, 3, 2); ''')
cursor.execute(''' insert into TakeOrder (seller_id, PVZ_id, buyer_id) values ( 4, 3, 3); ''')
cursor.execute('''insert into TakeOrder (seller_id, PVZ_id, buyer_id) values ( 5, 1, 4); ''')
cursor.execute('''insert into TakeOrder (seller_id, PVZ_id, buyer_id) values ( 6, 1, 1); ''')


takeorder = cursor.execute("""select order_id, ProductName,productprice,firstname,secondname,pvz_id, status from TakeOrder
inner join buyer on TakeOrder.BUYER_id = buyer.id
inner join seller on TakeOrder.seller_id = seller.id
inner join PVZ on TakeOrder.PVZ_id = PVZ.id
 """)

result1=takeorder.fetchall()
print(*result1, sep='\n')

connection.commit()
connection.close()