import time

from connection import MongoDBConnection
import datetime

DATABASE_NAME = "AssignDB"
COLLECTION_NAME = "todolist"
DB_URL = "mongodb://localhost:27017/"

coll_obj = MongoDBConnection(DATABASE_NAME, COLLECTION_NAME, DB_URL).create_connection()  # creating objection


# insert todo task
def insert_todo(**kwargs):
    '''
    :param kwargs:
    :return: None
    '''

    if coll_obj is not None:
        data = kwargs
        data['createdDate'] = datetime.datetime.now()
        data['timestamp'] = datetime.datetime.now()
        try:
            response = coll_obj.insert_one(data)
            print(f'inserted {response.acknowledged} and {response.inserted_id}')
        except Exception as e:
            print(e)


def find_todo(id=None, title=None, cardColor=None):
    if coll_obj is not None:
        try:
            if id is not None:
                resultSet = coll_obj.find({"id": id})
                for data in resultSet:
                    print(data)
                return resultSet
            elif title is not None:
                query = {"title": {"$regex": title, "$options": "i"}}
                resultSet = coll_obj.find(query)
                for data in resultSet:
                    print(data)
            else:
                resultSet = coll_obj.find({}, {"_id": 0})
                for data in resultSet:
                    print(data)
        except Exception as e:
            print(e)
    else:
        return None


def delete_todo(todo_id):
    if coll_obj is not None:
        document: dict = find_todo(id=todo_id)
        if document:
            response = coll_obj.delete_one({"id": todo_id})
            print(response.acknowledged, response.deleted_count)
        else:
            raise Exception(f"couldn't find any document with id {todo_id}")


def update_todo(todo_id):
    if coll_obj is not None:
        document: dict = find_todo(id=todo_id)
        if document:
            field_name = input("enter the field name: ")
            field_value = input("enter field value to update: ")
            if field_name == "isCompleted":
                field_value = True if field_value.lower() == 'true' else False
            date = {field_name: field_value, "timestamp": datetime.datetime.now()}
            response = coll_obj.update_one({"id": todo_id}, {"$set": date})
            print(response.acknowledged, response.modified_count)
        else:
            raise Exception(f"couldn't find any document with id {todo_id}")


def main():
    while True:
        print("*" * 30)
        print('1.insert\n 2.find\n 3.find on id\n 4. find on title\n 5.update on id\n 6. delete on id\n 7.-1 : exit\n ')
        print("*" * 30)
        choice = int(input('Enter the choice: '))
        if choice == 1:
            id = int(input("enter id: "))
            title = input("enter task name: ")
            cardColor = input("Enter task status : Red , Blue , Green: ")
            isCompleted = input('Is task Completed? true / false: ')
            isCompleted = True if isCompleted == 'true' else False
            insert_todo(id=id, title=title, cardColor=cardColor, isCompleted=isCompleted)
        elif choice == 2:
            find_todo()
        elif choice == 3:
            id = int(input("enter the task id: "))
            find_todo(id)
        elif choice == 4:
            title = input("enter the title name: ")
            find_todo(title=title)

        elif choice == 5:
            todo_id = int(input("enter task id: "))
            update_todo(todo_id)

        elif choice == 6:
            todo_id = int(input("enter task id: "))
            delete_todo(todo_id)
        elif choice == -1:
            break


if __name__ == '__main__':
    main()
