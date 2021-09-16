from flask import Flask, jsonify, request, current_app
#from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
import time
#from loguear import loguea

#db = SQLAlchemy()


def create_app(settings_module):
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
#    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:testing@localhost:5432/miniblog'
#    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # login_manager.init_app(app)
    #login_manager.login_view = "login"

    # db.init_app(app)

    # Custom error handlers
    # register_error_handlers(app)

    return app


def checkdata(postedData):
    current_app.logger.info("verifica datos")
    from dbmongo.models import Mensaje
    ts = time.time()
    print("el tipo es ")
    print(type(ts))
    s1 = Mensaje(ts=time.time(), texto='Verifica data')
    s1.save()
    current_app.logger.info("save ")
    estate = 200
    if "x" not in postedData or "y" not in postedData:
        estate = int(301)
        print("falta uno")
        return estate
    else:
        a = postedData["x"]
        b = postedData["y"]

        if not type(a) == int:
            estate = 301
            print("x mal")
            return estate

        if not type(b) == int:
            estate = 301
            print("y mal")
            return estate

    return estate


class Subtract(Resource):
    def post(self):

        # Step 1 get posted data
        retJson = {}
        mess = "Error con los datos recibidos"
        postedData = request.get_json()
        # Step 1 valid los data
        status_code = checkdata(postedData)
        current_app.logger.info("resta 2 nros")
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
        current_app.logger.info("suma 2 nros")
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
