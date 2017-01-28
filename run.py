"""Simple Migrator."""
__author__ = 'bkzhn'

connection_string = 'mysql+pymysql://root:1234@localhost/test'


def get_tables(connection):
    """Function to get all tables in db."""
    sql = 'SHOW TABLES;'
    result = connection.execute(sql)
    tables = list()

    for row in result:
        tables.append(row[0])

    return tables


def get_columns(connection, table):
    """Function to get columns information."""
    sql = 'DESCRIBE ' + table + ';'
    result = connection.execute(sql)
    columns = list()

    for row in result:
        column_name = row[0]
        column_type = row[1].split('(')
        column_type = column_type[0]

        column = {
            'name': column_name,
            'type': column_type
        }

        columns.append(column)

    return {
        table: columns
    }


def dump_to_json(tables):
    """Function to dump db structure to json."""
    import json

    with open('db.json', 'wb') as f:
        j = json.dumps(tables, f, indent=2)
        f.write(bytes(j, 'UTF-8'))


if __name__ == '__main__':
    print('== Simple Migrator ==')
