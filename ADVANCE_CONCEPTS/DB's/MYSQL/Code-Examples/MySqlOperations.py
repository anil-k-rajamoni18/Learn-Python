from DBConnection import SQLDBConnection
from SqlConstants import Queries

# database object creation.
sqlObj = SQLDBConnection('mayUser', 'MayDB@18', 'RocketCars', 'localhost').create_dbconnection()

# cursor object creation for doing all CRUD operations.
cursor = sqlObj.cursor()

def sql_info():
    print(f' IS Connected to Server: {sqlObj.is_connected()} ')
    print(f' MYSQL Server version {sqlObj.get_server_info()} ')
    print(f' Logged in user: {sqlObj.user} ')
    print(f' Connected DataBase Name: {sqlObj.database} ')

def show_dbs():
    cursor.execute(Queries.SHOW_DATABASES) # returns cursor object.

    # display results
    for table_name in cursor:
        print(table_name)

def show_tables():
    cursor.execute(Queries.SHOW_TABLES) # returns cursor object.

    # display results
    for table_name in cursor:
        print(table_name)


def create_database():
    try:
        cursor.execute(Queries.CREATE_DATABASE)
        print(f' Created Database successfully .......')
    except Exception as e:
        sqlObj.rollback()
        print(f'Issue occured , couldnt completed operation {e}')


def create_table():
    try:
        cursor.execute(Queries.CREATE_TABLE)
        print(f' Created Table successfully .......')
    except Exception as e:
        sqlObj.rollback()
        print(f'Issue occured , couldnt completed operation {e}')


def insert_one():
    query = Queries.INSERT_ONE.format('ford maverick',15, 6, 250, 72, 3158, 19.5, '1975-01-01', 'USA')
    print(query)

    try:
        cursor.execute(query)

        sqlObj.commit()
        print('Inserted row.... data successfully...')
    except Exception as e:
        sqlObj.rollback()
        print(f' issue occure while insertion.. {e}')

        
def insert_many():
    try:
        cursor.execute(Queries.INSERT_MANY)

        sqlObj.commit()
        print(cursor.rowcount, "record inserted.")

    except Exception as e:
        print(f"issue occured while insertion , {e}")



def retrieve_data():
    try:
        cursor.execute(Queries.SELECT_ALL_CARS)

        resultSet = cursor.fetchall()

        for row in resultSet:
            print(row)

    except Exception as e:
        print(f'issue occured while reading data from table ... {e}')


def update_one():
    pass

def update_many():
    pass

def delete_one():
    pass

def delete_many():
    pass


if __name__ == '__main__':
    #sql_info()
    #show_dbs()
    #show_()tables
    # create_database()
    #create_table()
    #insert_one()
    #insert_many()
    retrieve_data()
