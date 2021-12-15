import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import logging
from flask_mail import Mail

api = Api()
db = SQLAlchemy()
logging.basicConfig(level=logging.INFO, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
mailsender = Mail()

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
    api.add_resource(controllers.EmpresaController, '/empresa/<id>')
    api.add_resource(controllers.EmpresasController, '/empresas')
    api.add_resource(controllers.ApuestaController, '/apuesta/<id>')
    api.add_resource(controllers.ApuestasController, '/apuestas')
    api.add_resource(controllers.CuotaController, '/cuota/<id>')
    api.add_resource(controllers.CuotasController, '/cuotas')
    api.add_resource(controllers.ApuestaGanadaController, '/apuesta-ganada/<id>')
    api.add_resource(controllers.ApuestasGanadasController, '/apuestas-ganadas')

    api.init_app(app)

    from main.mail import functions
    app.register_blueprint(mail.functions.mail)

    app.config['MAIL_HOSTNAME'] = os.getenv('MAIL_HOSTNAME')
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['FLASKY_MAIL_SENDER'] = os.getenv('FLASKY_MAIL_SENDER')

    mailsender.init_app(app)

    return app