from sqlalchemy import Table, Column, Integer, Unicode, MetaData, create_engine, insert, select
from sqlalchemy.orm import mapper, create_session, sessionmaker

# подключаемся к бд
engine = create_engine("postgresql://postgres:postgres@localhost:5432/testdb", echo = False, future=True)
# кладем в Meta метаданные подгруженные из БД
meta = MetaData(engine)
# описываем какие таблицы хотим выгрузить из meta
table_list=['example_coins', 'example_coins1']

#создаем словарь для хранения экземпляра класса
instance_dict= {}
for t in table_list:
    instance_dict[t] = Table(t, meta, autoload=True)
print(instance_dict)

record_dict = {'bitcoin' : 'hueta', 'dogecoin' : "parasha"}

# делаем запись в БД для каждой таблицы
with engine.connect() as connection:
    for t in table_list:
        insert_query = instance_dict[t].insert().values([record_dict])
        print(insert_query)
        connection.execute(insert_query)
    connection.commit()

