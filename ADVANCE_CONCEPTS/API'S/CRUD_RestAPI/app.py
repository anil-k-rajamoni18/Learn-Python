from flask import Flask , request
from DBModules.CLient import *

app = Flask(__name__)

mycoll  = CreateConnection('Restaurant','fooditems')

print("COnnection successfull...")

@app.route("/")
def index():
  return "<h2><center> Greetings from rest mirco services... </center></h2>"


@app.route("/foods")
def getFoods():
    data = mycoll.find()
    responseData = []
    for dt in data:
      responseData.append(dt)
    return {"data":responseData}

@app.route("/foods/<id>")
def getOneFoodItem(id):
  data = mycoll.find({'_id': int(id)})
  if data:
    responseData = []
    for dt in data:
      responseData.append(dt)
    return {"data":responseData}
  return {"data":"no record found."}


@app.route("/foods",methods=["POST"])
def getDrinks():
  if request.method=="POST":
    data = request.get_json()
    print(type(data))
    data = mycoll.insert_one(data)

    return {"data":data.inserted_id}

@app.route("/foods/<id>" ,methods=["DELETE"])
def deletFoodItem(id):
  if request.method == "DELETE":
    data = mycoll.find_one({"_id":int(id)})
    if data:
      res = mycoll.delete_one({"_id":int(id)})
      return {"data": f"deleted record with count {res.deleted_count} {res.acknowledged}"}
    else:
      return {"data":"no record with id"}

@app.route("/foods/<id>",methods=["PUT"])
def updateFoodItem(id):
  if request.method == "PUT":
    data = mycoll.find_one({"_id":int(id)})
    if data:
      responseData = request.get_json()
      filter = {"_id":int(id)}
      new_values = {"$set":responseData}
      returnResponse = mycoll.update_one(filter,new_values)
      return {"data":returnResponse.acknowledged}

    else:
      return {"data": "no record with id."}




if __name__ == '__main__':
  app.run(port='1122',debug=True)
