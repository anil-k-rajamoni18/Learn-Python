from DBUtility import MongoDBConnection
import datetime
collObj = MongoDBConnection('ProjectDB','todolist_coll','mongodb://localhost:27017/').create_connection()
print(collObj)


#CRUD OPERATOR 
def insert_todo(**kwargs):
    if collObj is not None:
        data = kwargs
        data['createdDate'] = datetime.datetime.now()
        try:
            response = collObj.insert_one(data)
            print(f'inserted {response.acknowledged} and {response.inserted_id}')
        except Exception as e:
            print(e)



def find_todo(id=None,title=None,cardColor=None):
    if collObj is not None:
        try:
            if id is not None:
               resultSet = collObj.find({"id" : id})
               for data in resultSet:
                   print(data)
            elif title is not None:
               resultSet = collObj.find({"title" : title})
               for data in resultSet:
                   print(data)
            else:
               resultSet = collObj.find({},{"_id": 0})
               for data in resultSet:
                   print(data)
        except Exception as e:
            print(e)
    else:
        return None


def delete_todo(id):
    pass

def update_todo(todo_id):
    pass


def main():
    while True:
        print("*"*30)
        print('1.insert\n 2.find\n 3.find on id\n 4. find on title\n 5.update on id\n 6. delete on id\n 7.-1 : exit\n ')
        print("*"*30)
        choice = int(input('Enter the choice: '))
        if choice == 1:
            id = int(input("enter id: "))
            title = input("enter task name: ")
            cardColor = input("Enter task status : Red , Blue , Green: ")
            isCompleted = input('Is task Completed? true / false: ')
            isCompleted = True if isCompleted == 'true' else False
            insert_todo(id = id , title = title , cardColor = cardColor, isCompleted = isCompleted)
        elif choice ==2:
            find_todo()

        elif choice == -1:
            break

if __name__ == '__main__':
    main()