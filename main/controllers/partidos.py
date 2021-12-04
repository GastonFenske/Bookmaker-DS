from .. import db
from flask_restful import Resource
from main.models import PartidoModel
from flask import request, jsonify
from main.map import PartidoSchema
from main.repositories import PartidoRepositorio
from main.services import PartidoService

partido_schema = PartidoSchema()
partido_repositorio = PartidoRepositorio()

class Partido(Resource):
    def get(self, id):
        partido = db.session.query(PartidoModel).get_or_404(id)
        try:
            return partido_schema.dump(partido), 201
        except:
            return '', 404

    def delete(self, id):
        partido = db.session.query(PartidoModel).get_or_404(id)
        try:
            db.session.delete(partido)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        partido = db.session.query(PartidoSchema).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(partido, key, value)
        try:
            db.session.query(partido)
            db.session.commit()
            return partido_schema.dump(partido), 201
        except:
            return '', 404

class Partidos(Resource):

    def get(self):
        partidos = db.session.query(PartidoModel).all()
        return partido_schema.dump(partidos, many=True)

    # def post(self):
    #     partido = partido_schema.load(request.get_json())
    #     db.session.add(partido)
    #     db.session.commit()
    #     return partido_schema.dump(partido), 201

    def post(self):
        """"""
        services = PartidoService()
        partido = partido_schema.load(request.get_json())
        return services.agregar_partido(partido)

