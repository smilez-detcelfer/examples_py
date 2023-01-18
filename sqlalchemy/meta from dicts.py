from sqlalchemy import BigInteger, Boolean, Column, DateTime, Integer, Text
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

_type_lookup = {
    'bigint': BigInteger,
    'boolean': Boolean,
    'default': '',
    'index': True,
    'int': Integer,
    'required': False,
    'text': Text,
    'timestamptz': DateTime(timezone=True),
    'unique': True,
    'values': Text
}


def convert_table_classname(name):
    return ''.join(x.capitalize() or '_' for x in name.split('_'))


def mapping_for_json(schema):
    for table_key, table_values in schema.items():

        for table_name, col_data in table_values.items():

            json_cls_schema = {'tablename': table_name,
                               'columns': [{'name': 'id', 'type': Integer, 'is_pk': True}]}

            for col_name, constraints in col_data.items():
                new_col = {'name': col_name}

                if 'type' in constraints and constraints['type'] in _type_lookup:
                    new_col.update({'name': col_name, 'type': _type_lookup[constraints['type']]})

                if 'default' in constraints:
                    _type_lookup.update({'default': constraints['default']})

                for x in constraints:
                    if x != 'type' and x in _type_lookup:
                        new_col.update({'name': col_name, 'type': _type_lookup[constraints['type']], x: _type_lookup[x]})

                json_cls_schema['columns'].append(new_col)

            clsdict = {'clsname': convert_table_classname(table_name), '__tablename__': json_cls_schema['tablename']}

            clsdict.update(
                {record['name']: Column(
                    record['type'],
                    primary_key=record.get('is_pk', False),
                    nullable=record.get('required', False),
                    unique=record.get('unique', False),
                    default=record.get('default', False)
                )
                    for record in json_cls_schema['columns']
                }
            )

            e = create_engine("sqlite://", echo=True)
            type(clsdict['clsname'], (Base,), clsdict)
            Base.metadata.create_all(e)


if __name__ == "__main__":
    json_data = {"groupings": {
        "imaging": {
            "owner": {"type": "bigint", "required": True, "index": True},
            "tags": {"type": "text", "default": "#00C7FF"},
            "filename": {"type": "text"},
        },

        "user": {
            "email": {"type": "text", "required": True, "unique": True},
            "name": {"type": "text"},
            "role": {
                "type": "text",
                "required": True,
                "values": [
                    "admin",
                    "customer",
                ],
                "index": True
            },
            "date_last_logged": {"type": "timestamptz"}
        }
    }
    }

    mapping_for_json(json_data)