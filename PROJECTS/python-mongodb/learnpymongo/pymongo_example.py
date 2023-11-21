import pymongo

connection_url = "mongodb://127.0.0.1:27017"

client = pymongo.MongoClient(connection_url)  # client object creation


def server_info():
    print(client.HOST)
    print(client.PORT)
    print(client.server_info())
    print(client.address)


# server_info()

def list_database_names():
    for database in client.list_databases():
        print(database)


# list_database_names()


def create_database():
    mydb = client['MarvelsDB']
    mycoll = mydb['movies_coll']
    response = mycoll.insert_one({"name": "Guardian of Galaxy VOL3", "year": "2023", "collections": 2.3})
    print(response.acknowledged, response.inserted_id)


# create_database()


def drop_database(name):
    client.drop_database(name)
    print(f'dropped {name} successfully')


# drop_database('MarvelsDB')


def connect_to_existing_database():
    db_name = input("enter database name: ")
    dblist = client.list_database_names()
    print(dblist)

    try:
        if db_name in dblist:
            print("The database exists.")
            mydb = client[db_name]  # creates db object

            coll_name = input('enter collection-name: ')
            collList = mydb.list_collection_names()
            try:
                if coll_name in collList:
                    mycoll = mydb['coll_name']
                    # require operations
                else:
                    raise Exception('collection not found..')

            except Exception as e:
                print(e)
        else:
            raise Exception("DB not found ..")
    except Exception as e:
        print(e)


# connect_to_existing_database()


def create_collection():
    db = client['demodb']
    coll = db['customers']
    response = coll.insert_one({"name": "kumar", "place": "hyd"})
    print(response.inserted_id, response.acknowledged)
    print(db.list_collection_names())


# create_collection()


def drop_collection(coll_name, db_name):
    db = client[db_name]
    response = db.drop_collection(coll_name)
    print(response)
    print(f'dropped {coll_name}')


# drop_collection('customers', 'demodb')


def find_operation():
    db = client['training']
    coll = db['vintage_cars']

    # print(coll.find_one())
    # for car in coll.find(): # list of documents
    #     print(car)

    # find all cars having horsepower greater than 220
    query = {"Horsepower": {"$gt": 220}}
    response = coll.find(query)
    for car in response:
        print(car)

    # find all cars from Japan
    query1 = {"Origin": "Japan"}

    # find all country names


# find_operation()

def update_operation():
    db = client['collegedb']
    coll = db['student']

    # update one
    # data = {"course": "Azure Cloud"}
    # response = coll.update_one({"_id": 2}, {"$set": data})
    # print(response.acknowledged, response.modified_count)

    # update multiple
    data = {"fee": 27000}
    filter_con = {"course": 'java'}
    response = coll.update_many(filter_con, {"$set": data})
    print(response.matched_count)


# update_operation()


def delete_operation():
    db = client['collegedb']
    coll = db['student']
    filter_con = {"name": 'joyce'}
    response = coll.delete_one(filter_con)
    print(response.deleted_count)


delete_operation()
