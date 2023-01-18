#pip3 install sqlalchemy
#pip3 install psycopg2
from sqlalchemy import create_engine, Table, Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import multiprocessing

# строка подключения к БД:
engine = create_engine("postgresql://postgres:postgres@localhost:5432/testdb", echo = True)
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()

#описание таблицы в БД
class Dogcoin(Base):
    __tablename__ = 'dogcoin'
    tran_id = Column(Numeric)
    price = Column(Numeric)
    column3 = Column(String(250))

# строка ниже создаст все описанные объекты БД, раскоментить для создания
Base.metadata.create_all(engine)

# в цикле ловим json
# превращаем json в список кортежей

parsed_json = [(1, 36.7, 'blaaaa'),
          (2, 38.0, 'bsdf'),
          (3, 39.1, 'csdfs')]

def insert():
    #try:

    dicts = [dict(tran_id=t[0], price=t[1], column3=t[2]) for t in parsed_json]
    # [(tran_id = 1; price = 32.4, col3 = 'somedata), (tran_id = 2; price = 32.4, col3 = 'somedata)]
    
    session.bulk_insert_mappings(Dogcoin, dicts)
    session.commit()
        # добавить прерывание если запрос работает дольше n секунд
    #except:
        # записать в файл если insert не удался


# запускаем сабпроцесс с вызовом insert
# вот здесь нужен какой-то генератор переменной

# if __name__ == '__main__':
#     insert_subprocess = multiprocessing.Process(target=insert, args=())
#     insert_subprocess.start()