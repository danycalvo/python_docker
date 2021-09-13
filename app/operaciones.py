from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from app import checkdata

class Subtract(Resource):
    def post(self):

        # Step 1 get posted data
        retJson = {}
        mess = "Error con los datos recibidos"
        postedData = request.get_json()
        # Step 1 valid los data
        status_code = checkdata(postedData)
        if status_code != 200:
            retJson = {
                'Message': mess,
                'Status ': status_code
            }
            retMap = jsonify(retJson)
        else:
            x = postedData["x"]
            y = postedData["y"]
            x = int(x)
            y = int(y)

            # Step 2 Add the posted data
            ret = x - y
            retMap = {
                'Sum': ret,
                'Status code': 200
            }
            return jsonify(retMap)



class Add(Resource):
    def post(self):

        # Step 1 get posted data
        retJson = {}
        errore = "Error de datos"
        mess = "Error con los datos recibidos"
        postedData = request.get_json()
        # Step 1 valid los data
        status_code = checkdata(postedData)
        print(status_code)
        if status_code == 301:
            print(" status code paso 301")
            print("paso 301")
            retJson = {
                'Message': "error ",
                'Status ': 301
            }
            print("301 error")
            print(retJson)
            retMap = jsonify(retJson)
            print(retMap)
            print("301 error print retMap arriba")
            retMap = {
                'Resultado': errore,
                'Status code': 301
            }
            # return jsonify(retMap)
        else:
            print("else status code paso 200")
            x = postedData["x"]
            y = postedData["y"]
            x = x
            y = y

            # Step 2 Add the posted data
            ret = x + y
            retMap = {
                "El resultado es:" + ':': ret,
                'Status code': 200
            }

        return jsonify(retMap)
