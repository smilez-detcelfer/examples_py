from sqlalchemy import Table, Column, Integer, Unicode, MetaData, create_engine
from sqlalchemy.orm import mapper, create_session, sessionmaker

# подключаемся к бд
engine = create_engine("postgresql://postgres:postgres@localhost:5432/testdb", echo = True)
# кладем в Meta метаданные подгруженные из БД
metadata = MetaData(engine)
# список названий колонок (может быть любой itterable объект со строками)
col_list = ['bitcoin', 'lightcoin', 'dogecoin', 'shitcoin', 'newcoin']

# описываем метаданные таблицы:
table_meta = Table('coins1', metadata, Column('id', Integer, primary_key=True),
                   *(Column(coin_name_col, Unicode(255)) for coin_name_col in col_list))

# создаем таблицу в БД по созданному описанию
metadata.create_all()
#---------------------------------------------------

# создаем класс таблицы:
class Table_class(object):
    pass
#создаем мапинг класса таблицы и описания
mapper(Table_class, table_meta)
# после mapper можно обращаться так:
t = Table_class
t.colname = 'record in colname'
t.colname1 = 'record in colname1'

#открываем сессию, добавляем экземпляры класса TableClass и записываем в БД
session = create_session(bind=engine, autocommit=False, autoflush=True)
session.add(t)
session.commit()
