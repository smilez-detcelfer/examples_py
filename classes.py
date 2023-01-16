


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
            print(attribute, '=', value)


column_list = ['col1', 'col2', 'col3']
table = Table('tablename', 'sche1', column_list)

table.display()
# print(table.c_col1.c_name
table.c_col1.name = '123'
table.c_col1.display()
print(isinstance(table.c_col1, Column))

