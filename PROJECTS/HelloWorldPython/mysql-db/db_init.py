from db_connection import connection
from queries import Queries


def server_related_info():
    print(connection)
    print(dir(connection))

    # server information
    print(connection.get_server_info())
    print(connection.is_connected())
    # print(connection.ping())
    # print(connection.config())
    print(connection.server_host)
    print(connection.server_port)
    print(connection.database)
    print(connection.sql_mode)


# server_related_info(connection)


def create_table_operation():
    cursor = connection.cursor()
    response = cursor.execute(Queries.create_table_query)
    print(response)
    print(f'Query executed successfully')
    cursor.close()


# create_table_operation()

def insert_data_operation():
    cursor = connection.cursor()
    result_set = cursor.execute(Queries.insert_query)
    print(f'query executed successfully {result_set}')
    connection.commit()
    cursor.close()


# insert_data_operation()


def insert_operation_with_parametes(values: list) -> None:
    cursor = connection.cursor()
    cursor.execute(Queries.insert_param_query, values)
    print(f'{cursor.rowcount} rows inserted.')

    connection.commit()
    cursor.close()


# data = [2, 'Bob', 'EEE', 'University of Florida', 'FL', 'M', '2021', '2025-04-30']
# insert_operation_with_parametes(data)


def insert_multiple_records(data: list[list]) -> None:
    cursor = connection.cursor()
    cursor.executemany(Queries.insert_param_query, data)
    print(f'{cursor.rowcount} rows inserted.')

    connection.commit()
    cursor.close()


data = [
    [3, 'Charlie', 'Mechanical', 'Michigan University', 'MC', 'M', '2023', '2027-06-15'],
    [4, 'David', 'Civil', 'Chicago University', 'CO', 'M', '2020', '2024-08-18'],
    [5, 'Eva', 'Biotechnology', 'Princeton University', 'NY', 'F', '2022', '2026-11-22'],
    [6, 'Frank', 'Chemistry', 'Michigan University', 'MC', 'M', '2021', '2025-09-10']
]


# insert_multiple_records(data)

def select_operation():
    cursor = connection.cursor()
    cursor.execute(Queries.select_all_query)
    result_set = cursor.fetchall()

    # print(result_set, type(result_set))
    for row in result_set:
        print(row)


select_operation()
