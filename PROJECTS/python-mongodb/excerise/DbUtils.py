def insert_one_document(coll, data):
    return coll.insert_one(data)


def insert_multiple(coll, data: list[dict]):
    return coll.insert_many(data)

