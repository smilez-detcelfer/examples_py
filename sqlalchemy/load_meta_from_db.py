from sqlalchemy import Table, Column, Integer, Unicode, MetaData, create_engine, insert
from sqlalchemy.orm import mapper, create_session, sessionmaker

# подключаемся к бд
engine = create_engine("postgresql://postgres:postgres@localhost:5432/testdb", echo = True, future=True)
# кладем в Meta метаданные подгруженные из БД
meta = MetaData(engine)
# описываем какие таблицы хотим выгрузить из meta
coins = Table('coins', meta, autoload=True)

# можем посмотреть метаданные из подгруженной таблицы, например данные колонок
coins_cols = coins.c
for i in coins_cols:
    print(i.name, i.type)

# делаем запись в БД
insert_query = coins.insert().values([
    {'bitcoin' : 'hueta', 'lightcoin' : "parasha"},
    {'bitcoin' : "hueta1", 'lightcoin' : "parasha1"},
    ])
print(insert_query)

with engine.connect() as connection:
    connection.execute(insert_query)
    connection.commit()
