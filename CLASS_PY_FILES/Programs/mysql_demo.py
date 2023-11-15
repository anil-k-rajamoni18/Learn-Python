import mysql.connector as mysql

config = {
    'host': 'localhost',
    'user': 'root',
    'port': 3306,
    'password': 'DbAk@18',
    'database': 'classicmodels'
}

connection = mysql.connect(**config) # connection
print(connection.is_connected())

cursor = connection.cursor() # cursor 

select_query = """SELECT * FROM employees LIMIT 10"""

cursor.execute(select_query) # executing the query

for row in cursor.fetchall():
    print(row)