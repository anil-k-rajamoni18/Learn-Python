class Queries(object):

    create_table_query: str = """
    CREATE TABLE student (
        student_id INT PRIMARY KEY ,
        name VARCHAR(20) NOT NULL,
        stream VARCHAR(20) NOT NULL,
        college VARCHAR(40) NOT NULL,
        address VARCHAR(40) NOT NULL , 
        gender CHAR(1) NOT NULL,
        joined_year YEAR,
        graduation DATE
		);
	"""

    insert_query: str = """
    INSERT INTO student VALUES(1,'Kumar','IT', 'University of Texas', 'Texas', 'M', '2021', '2023-01-01')
    """

    insert_param_query = """
    INSERT INTO student(student_id, name, stream, college, address, gender, joined_year, graduation) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    select_all_query = """ SELECT * FROM student """

