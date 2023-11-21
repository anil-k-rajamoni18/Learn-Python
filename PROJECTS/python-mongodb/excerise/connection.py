import pymongo

connection_url = "mongodb://127.0.0.1:27017"

client = pymongo.MongoClient(connection_url)  # client object creation


def connect_to_existing_database(db_name, coll_name):
    dblist = client.list_database_names()
    print(dblist)

    try:
        if db_name in dblist:
            print("The database exists.")
            mydb = client[db_name]  # creates db object

            collList = mydb.list_collection_names()
            try:
                if coll_name in collList:
                    mycoll = mydb['coll_name']
                    print(f'cursor pointing {db_name} , {coll_name}')
                    return mycoll
                else:
                    raise Exception('collection not found..')

            except Exception as e:
                print(e)
        else:
            raise Exception("DB not found ..")
    except Exception as e:
        print(e)


def creation_new_connection(db_name, coll_name):
    db = client[db_name]
    coll = db[coll_name]
    print(f'cursor pointing {db_name} , {coll_name}')
    return coll
