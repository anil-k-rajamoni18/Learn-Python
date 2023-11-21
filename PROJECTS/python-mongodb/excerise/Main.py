from connection import  connect_to_existing_database, creation_new_connection
from apiUtils import get_cars_data
from DbUtils import insert_multiple

coll_obj = creation_new_connection('training', 'vintage_cars')
car_data = get_cars_data()

# print(car_data)

response = insert_multiple(coll_obj, car_data)
print(response)
