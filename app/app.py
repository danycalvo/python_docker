from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import os
import json
#from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine
from funciones import create_app, checkdata
from funciones import Add, Subtract

data = os.environ.get('MI_DATA', 'Result:')
settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)
app.config['MONGODB_SETTINGS'] = {
    'db': 'pythonlog',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)
#app.config['DEBUG'] = True
api = Api(app)
app.logger.info("inicio app")


def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
        return 500
    #        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return 404
    #     return render_template('404.html'), 404


api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')


@app.route("/")
def hello_world():
    return "Hello, World!", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')

# curl -X POST -H "Content-Type: application/json" -d '{"x": 2, "y": 7}' http://127.0.0.1:5000/add
# curl -X POST -H "Content-Type: application/json" -d '{"x": 2, "y": 7}' http://192.168.0.223:5000/add
# curl -X POST -H "Content-Type: application/json" -d '{"x": 12, "y": 7}' http://192.168.0.223:5000/subtract
# https://blog.entirely.digital/docker-gunicorn-and-flask/
# https://github.com/danycalvo/python_docker.git
# https://github.com/danycalvo/python_docker/
