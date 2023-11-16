class SqlQueries(object):
    CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS car_data (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255),
        miles_per_Gallon FLOAT,
        cylinders INT,
        displacement INT,
        horsepower INT,
        weight_in_lbs INT,
        acceleration FLOAT,
        year DATE,
        origin VARCHAR(255)
        );
    """

    INSERT_QUERY = """
    INSERT INTO car_data(name,miles_per_Gallon,cylinders,displacement,horsepower,weight_in_lbs,acceleration,year,origin)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    SHOW_TABLES = "show tables"