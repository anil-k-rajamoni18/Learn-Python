import mysql.connector as mysql

class SQLDBConnection:
    def __init__(self, username, password, database,host):
        self.__dbusername = username
        self.__dbpassword = password
        self.__database = database
        self.__host = host
        self.__mydb = None
        self.__mycurosr = None

    def create_dbconnection(self):

        try:
            self.__mydb = mysql.connect(
                host = self.__host,
                user = self.__dbusername,
                password = self.__dbpassword,
                database = self.__database,
                auth_plugin='mysql_native_password'
            )
        except Exception as e:
            print(e)
            print('Exception occured while creating connection ... ')

        return self.__mydb
    def create_cursor(self):
        if self.__mydb != None:
            self.__mycurosr = self.__mydb.cursor()
            return self.__mycurosr
        else:
            print('Error in creating cursor object...')



# connObj = SQLDBConnection('root', 'SqlAk@18', 'food','localhost')

# result = connObj.create_dbconnection()

# print(result.get_server_info())