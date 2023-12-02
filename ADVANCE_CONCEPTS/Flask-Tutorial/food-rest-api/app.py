from flask import Flask,request
from db.MongoUtils import MongoDBConnection


mycoll =  MongoDBConnection('rocketRecipeDB','food-items','mongodb://localhost:27017/').create_connection()

print(mycoll)

app = Flask(__name__)


env = {
    'name' : 'rocket recipe microservice',
    'version': 'V1.0'
}

@app.route('/')
def greet():
    return f"{env['name']} is UP & RUNNING with version : {env['version']}"

@app.get('/api/food/<int:id>')
def get_food_item(id):
    if mycoll is not None:
        data = mycoll.find_one({'_id': id})
        if data is not None:
            return data
        else:
            return {}


@app.get('/api/foods/')
def get_food_items():
    if mycoll is not None:
        data = [document for document in mycoll.find()]

        if data:
            return data
        else:
            return []


@app.post('/api/food/')
def save_food_item():
    if mycoll is not None:
        data = request.json # extract the dat in the form of dictionary 
        response = mycoll.insert_one(data)
        return f' data inserted successfully {response.acknowledged} {response.inserted_id}'
    return f'Service is not avaiable....'

@app.post('/api/foods/')
def save_food_items():
    pass

@app.put('/api/food/<int:id>')
def update_food_item():
    pass


@app.delete('/api/food/<int:id>')
def delete_food_item():
    pass


if __name__ == '__main__':
    # create db connection..
    app.run(debug=True)