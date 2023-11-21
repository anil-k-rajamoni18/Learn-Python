import pymongo

connection_url = "mongodb://127.0.0.1:27017/?directConnection=true"
client = pymongo.MongoClient(connection_url)

# for database in client.list_databases():
#     print(database)

# print(client.server_info())
# print(client.HOST)
# print(client.address)
# print(client.get_default_database())

# create database object

dbobj = client['collegedb']

# create collection object
collobj = dbobj['student']

# print(collobj.find_one())

# for document in collobj.find():
#     print(document)

data = {"name": "rolex", "course": "Dot Net", "fee": 1700}
result = collobj.insert_one(data)
print(result.acknowledged, result.inserted_id)
