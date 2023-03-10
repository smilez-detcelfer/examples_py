from sqlalchemy import Table, Column,  MetaData, create_engine
from sqlalchemy import Integer, Text, Boolean, BigInteger, DateTime

#SQLA connection
engine = create_engine("postgresql://postgres:postgres@localhost:5432/testdb", echo = True)
metadata = MetaData(engine)


#define table list and column list
table_list = ['coin_bitcoin', 'coin_lightcoin', 'coin_dogecoin']
column_list = [('rec_id', 'int'),
               ('timestamp', 'timestamptz'),
               ('sometext', 'bool'),
               *((f'column{n}', 'int') for n in range(3)),
               *((f'another_column{n}', 'bool') for n in range(3)),
               ]

#dictionary with column types
type_lookup = {
    'bigint': BigInteger,
    'bool': Boolean,
    'default': '',
    'index': True,
    'int': Integer,
    'required': False,
    'text': Text,
    'timestamptz': DateTime(timezone=True),
    'unique': True,
    'values': Text
}

# add description to metadata obj
for t in table_list:
    Table(t, metadata,
    Column('id', Integer, primary_key=True),
    *(Column(column_name, type_lookup[column_type]) for column_name, column_type in column_list))

# create data from metadata
metadata.create_all()