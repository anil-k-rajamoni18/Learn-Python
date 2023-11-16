import requests
from connection import conn
from queries import SqlQueries


def load_jsondata() -> list[dict]:
    api_url = "https://raw.githubusercontent.com/vega/vega/main/docs/data/cars.json"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            json_response = response.json()
            return json_response
    except Exception as ex:
        print(ex)


def create_table() -> None:
    cursor = conn.cursor()
    cursor.execute(SqlQueries.CREATE_TABLE)
    print(f'Table Created Successfully')

    cursor.execute(SqlQueries.SHOW_TABLES)
    print(cursor.fetchall())

    cursor.close()


def insert_data(data: list[dict]) -> None:
    cursor = conn.cursor()
    for entry in data: # iterating on list of dictionaries
        query = SqlQueries.INSERT_QUERY
        values = list(entry.values())
        cursor.execute(query, values)

        conn.commit()
        print(f'query executed {cursor.rowcount}')

    print('all records inserted')
    cursor.close()


api_response = load_jsondata() # load the data from api
create_table() # create table
insert_data(api_response) # insert the data
