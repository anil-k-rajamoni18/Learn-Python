import mysql.connector

# mysql configuration
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'DbAk@18',
    'database': 'nov_course_db',
}

# connection creation
connection = mysql.connector.connect(**config)
