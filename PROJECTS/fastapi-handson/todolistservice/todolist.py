import logging as log
import os

from fastapi import FastAPI, status

from dbconfig.connect import MongoDBConnection
from dbconfig.models import Response
from dbconfig.models import Todo

DATABASE_NAME = "trainingdb"
COLLECTION_NAME = "todolist"
DB_URL = os.getenv('MONGODB_URI')

coll_obj = MongoDBConnection(DATABASE_NAME, COLLECTION_NAME, DB_URL).create_connection()  # creating obj

# fast api obj creation
app = FastAPI()


# routes
@app.get(path="/")
async def health_check() -> dict:
    return {'status': 'ToDoList Service is UP & Running'}


@app.get(path="/api/todo/all", status_code=status.HTTP_200_OK)
async def get_todo_list() -> Response:
    log.info('invoking get todo list api')
    dbresponse = coll_obj.find({}, {"_id": 0})  # excluding _id: ObjectId(xxx) in response, due serialization problem
    todo_response = list(dbresponse) # dbresponse is cursor object, converting to list
    if todo_response:
        return Response(status="success", status_code=200, data=todo_response)
    else:
        return Response(status="no data", status_code=404, data=[], message="not data found for given request")


@app.get("/api/todo", status_code=status.HTTP_200_OK)
async def get_todo_by_title(title_name: str) -> Response:
    log.info('invoking get todo list by title-name api')
    query = {"title": {"$regex": title_name, "$options": "i"}}
    dbresponse = coll_obj.find(query, {"_id": 0})
    todo_response = list(dbresponse) # dbresponse is cursor object, converting to list
    if todo_response:
        return Response(status="success", status_code=200, data=todo_response)
    else:
        return Response(status="not data", status_code=404, data=[], message="not data found for given request")


@app.post("/api/todo", status_code=status.HTTP_201_CREATED)
async def save_todo(todo_item: Todo) -> Response:
    log.info('invoking post todo-list api')
    if todo_item is not None:
        print(todo_item, type(todo_item))
        dbresponse = coll_obj.insert_one(todo_item.model_dump())
        return Response(status="success", status_code=201, message=f'inserted id {dbresponse.inserted_id}')
    else:
        return Response(status="bad request", status_code=400)


@app.put("/api/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def update_todo(todo_id: int, todo_request: Todo) -> Response:
    log.info('invoking update todo-list api')
    dbresponse = coll_obj.update_one({"id": todo_id}, {"$set": todo_request.model_dump()})
    if dbresponse.modified_count:
        return Response(status="success", status_code=200, message='modified successfully')
    else:
        return Response(status="failed", status_code=404, message=f'no todo item with id {todo_id}')


@app.delete("/api/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def delete_todo(todo_id: int) -> Response:
    log.info('invoking delete todo-list api')
    dbresponse = coll_obj.delete_one({"id": todo_id})
    if dbresponse.deleted_count:
        return Response(status="success", status_code=200, message='deleted successfully')
    else:
        return Response(status="failed", status_code=404, message=f'no todo item with id {todo_id}')
