


class Column:

    def __init__(self, name, c_type, is_pk):
        self.name = name
        self.type = c_type
        self.is_pk = is_pk

    def display(self):
        print('column info:')
        print(f'name:{self.name} | type: {self.type} | pk: {self.is_pk}')


class Table:
    def __init__(self, name, schema, column_list_type1):
        self.name = name
        self.schema = schema
        self.c_id = Column('id', 'integer', True)
        self.c_time = Column('timestamp', 'bigint', False)
        for c in column_list_type1:
            setattr(self, f'c_{c}', Column(c, 'Numeric', False))

    def display(self):
        for attribute, value in self.__dict__.items():
            # if attribute[0] != 'c':
            print(attribute, '=', value)


column_list = ['col1', 'col2', 'col3']
table = Table('tablename', 'sche1', column_list)
table.display()
table.c_col1.display()

table_list = ['bitcoin', 'lightcoin', 'dogecoin']

instance_list = []
for i in table_list:
    instance_list.append(Table(i, 'sche1', column_list))

print(getattr(instance_list[0], 'name'))
