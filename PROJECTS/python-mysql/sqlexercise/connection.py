import mysql.connector as mysql  # alias importing

# create connection
config = {
    "host": "localhost",
    "user": "novuser",
    "password": "nov@123",
    "database": 'nov_course_db'
}
conn = None
try:
    conn = mysql.connect(**config)
    if conn.is_connected():
        print(f'connected successfully to database {conn.database}\nwith user: {conn.user}')
except Exception as e:
    print(f'exception occurred while establishing connection')
    print(e)

