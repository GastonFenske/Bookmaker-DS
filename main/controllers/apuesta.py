from flask_restful import Resource
from flask import request
from main.services import PartidoService
from main.map import ApuestaSchema, apuesta_schema
from .. import db

apuesta_schema = ApuestaSchema()


class Apuesta(Resource):
    def get(self):
        return PartidoService.obtener_partidos_no_finalizados()


class Apuestas(Resource):
    def post(self):
        """Metodo para crear una apuesta"""
        apuesta = apuesta_schema.load(request.get_json())
        db.session.add(apuesta)
        db.session.commit()
        return apuesta_schema.dump(apuesta)