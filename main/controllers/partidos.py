from .. import db
from flask_restful import Resource
from main.models import PartidoModel
from flask import request, jsonify

class Partido(Resource):
    def get(self, id):
        partido = db.session.query(PartidoModel).get_or_404(id)
        try:
            return partido.to_json()
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

class Partidos(Resource):

    def get(self):
        partidos = db.session.query(PartidoModel).all()

        return jsonify({
            'Partidos': [partido.to_json() for partido in partidos]
        })

    def post(self):

        partido = PartidoModel.from_json(request.get_json())
        db.session.add(partido)
        db.session.commit()
        return partido.to_json(), 201