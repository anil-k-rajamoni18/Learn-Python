class Queries:
    SHOW_DATABASES = ''' SHOW DATABASES'''
    SHOW_TABLES = '''SHOW TABLES'''
    CREATE_DATABASE = '''CREATE DATABASE IF NOT EXISTS RocketCars'''
    CREATE_TABLE = '''
                    CREATE TABLE IF NOT EXISTS cars(
                        id                  INTEGER AUTO_INCREMENT PRIMARY KEY,
                        Name                VARCHAR(30) NOT NULL,
                        Miles_per_gallon    INTEGER ,
                        Cylinders           INTEGER NOT NULL,
                        Displacement        INTEGER NOT NULL,
                        HorsePower          INTEGER NOT NULL,
                        Weight              INTEGER CHECK(weight>=100),
                        Acceleration        INTEGER NOT NULL,
                        Year                VARCHAR(10) NOT NULL,
                        Origin              VARCHAR(10) NOT NULL
                    )
                    '''
    INSERT_ONE = '''
                INSERT INTO cars(Name,Miles_per_gallon,Cylinders,Displacement,HorsePower,Weight,Acceleration,Year,Origin) 
                VALUES('{0}',{1},{2},{3},{4},{5},{6},{7},'{8}')
                 '''
    
    INSERT_MANY = '''
                INSERT INTO cars(Name,Miles_per_gallon,Cylinders,Displacement,HorsePower,Weight,Acceleration,Year,Origin) 
                VALUES('mercury monarch',15, 6, 250,72,3432,21,'1975-01-01','USA'),
                ('pontiac catalina',16, 8, 400,170, 4668, 11.5, '1975-01-01','USA')
                '''
    
    SELECT_ALL_CARS = ''' SELECT * FROM cars'''