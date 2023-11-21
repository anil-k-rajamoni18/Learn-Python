import requests


def get_cars_data():
    api_url = "https://raw.githubusercontent.com/vega/vega/main/docs/data/cars.json"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            json_data = response.json()
            print(f'call to api successfully, returning json data')
            return json_data
    except Exception as e:
        print(f'exception occured while calling api.{e}')
