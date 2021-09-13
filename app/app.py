from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from .operaciones import *
import pymongo
import os
import json

from app import create_app
from app import checkdata


settings_module = os.getenv('APP_SETTINGS_MODULE')
data = os.environ.get('MI_DATA', 'Result:')
url_db = os.environ.get('URL_DB')
print("Datos de la BD:")
##print(url_db)
print(settings_module)

app = create_app(settings_module)
#app = Flask(__name__)
#app.config['DEBUG'] = True
api = Api(app)


#myclient = pymongo.MongoClient(url_db)
#myclient = pymongo.MongoClient("mongodb://mongodb-26-rhel7:27017/")
#myclient = pymongo.MongoClient("mongodb://172.18.0.2:27017/")
#print(url_db)

#mydb = myclient["database"]
#mycol = mydb["clientes"]

print("Datos de la BD:")
print(url_db)
print(mydb)
print(mycol)

#mycol.insert_one()

#mistring = "Inserto en " + url_db + " " + mydb.name + " " + mycol.name

""""
class Mongo(Resource):
    def post(self):
        postedData = request.get_json()
        nom = postedData["Nombre"]
        eda = postedData["Edad"]
        mydict = {"name": nom, "Edad:": eda}
        x = mycol.insert(mydict)
        #x = mycol.insert_one(mydict)
        retMap = {
            'Mongo return': mistring,
            'Status code': 200
        }
        return jsonify(retMap)
"""

api.add_resource(Add, '/add')
api.add_resource(Mongo, '/mongo')
api.add_resource(Subtract, '/subtract')
@app.route("/")
def hello_world():
    return "Hello, World!", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')

# curl -X POST -H "Content-Type: application/json" -d '{"x": 2, "y": 7}' http://127.0.0.1:5000/add
# https://blog.entirely.digital/docker-gunicorn-and-flask/