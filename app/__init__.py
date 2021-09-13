from flask import Flask, jsonify, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()


def create_app(settings_module):
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:testing@localhost:5432/miniblog'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager.init_app(app)
    login_manager.login_view = "login"

    db.init_app(app)

    # Custom error handlers
    register_error_handlers(app)

    return app


def checkdata(postedData):

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

def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
             retrurn 500
    #        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
          return 404
    #     return render_template('404.html'), 404
