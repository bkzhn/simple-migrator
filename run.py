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


if __name__ == '__main__':
    print('== Simple Migrator ==')
