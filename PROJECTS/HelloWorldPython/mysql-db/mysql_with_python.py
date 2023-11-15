import mysql.connector

connection = None
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="novuser",
        password="nov@123",
        database='nov_course_db'
    )
    print(connection)
except Exception as ex:
    print(ex)

'''
print(connection.server_port)
print(connection.server_host)
print(connection.database)
print(connection.user)
print(connection.is_connected())
print(connection.get_server_info())
print(connection.get_server_version())
'''


def create_database():
    cursor = connection.cursor()  # creates cursor object, useful performing all trans
    query = 'CREATE DATABASE IF NOT EXISTS marveldb'
    cursor.execute(query)  # execute the query
    print(f'query executed successfully')
    cursor.close()


def show_databases():
    cursor = connection.cursor()
    query = '''show databases'''
    cursor.execute(query)
    print(cursor.fetchall())
    cursor.close()


def show_tables():
    cursor = connection.cursor()
    query = '''show tables'''
    cursor.execute(query)
    print(cursor.fetchall())
    cursor.close()


def drop_database(dbname):
    cursor = connection.cursor()
    query = f'''DROP DATABASE IF EXISTS {dbname}'''
    cursor.execute(query)
    print(f'query executed successfully')
    cursor.close()


def create_table(table_name):
    cursor = connection.cursor()
    query = f'''
    CREATE TABLE {table_name}(
    id INTEGER PRIMARY KEY ,
    name VARCHAR(40) NOT NULL,
    quantity INTEGER NOT NULL,
    price DECIMAL(10,3)
    );
    '''
    cursor.execute(query)
    print(f'created table successfully')
    show_tables()
    cursor.close()


def insert_data(table_name):
    cursor = connection.cursor()
    query = f'''
    INSERT INTO {table_name} (id,name,quantity,price) VALUES (1,'iphone13',5,78000);
    '''
    cursor.execute(query)
    print('data inserted successfully')
    connection.commit()
    cursor.close()


def insert_data_with_params(values):
    cursor = connection.cursor()
    query = '''
    INSERT INTO product_t values(%s,%s,%s,%s)
    '''
    cursor.execute(query, values)
    connection.commit()
    print(f'inserted successfully with query-params {cursor.rowcount}')
    cursor.close()


def insert_data_multiple(values):
    cursor = connection.cursor()

    # parameterized query
    query = '''
    INSERT INTO product_t values(%s,%s,%s,%s)
    '''
    cursor.executemany(query, values) # list of record/rows
    connection.commit()
    print(f'inserted successfully with query-params {cursor.rowcount}')
    cursor.close()


# show_databases()
# show_tables()
# drop_database('marveldb')

# create_table('product_t')

# insert_data('product_t')

# insert_data_with_params([2, 'ear pods3', 10, 25000])
# insert_data_with_params([3, 'ipad', 20, 88000])

product_data = [
    [4, 'samsung s21', 2, 53000],
    [5, 'realme GT', 6, 3300],
    [6, 'motorla neo', 10, 2700]
]

insert_data_multiple(product_data)
