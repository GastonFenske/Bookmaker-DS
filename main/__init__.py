import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    PATH = os.getenv("DATABASE_PATH")
    DB_NAME = os.getenv("DATABASE_NAME")
    if not os.path.exists(f'{PATH}{DB_NAME}'):
        os.mknod(f'{PATH}{DB_NAME}')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{PATH}{DB_NAME}'
    db.init_app(app)

    import main.controllers as controllers
    api.add_resource(controllers.ClientesController, '/clientes')
    api.add_resource(controllers.ClienteController, '/cliente/<id>')
    api.add_resource(controllers.PartidosController, '/partidos')
    api.add_resource(controllers.PartidoController, '/partido/<id>')
    api.add_resource(controllers.EquiposController, '/equipos')
    api.add_resource(controllers.EquipoController, '/equipo/<id>')

    api.init_app(app)

    return app