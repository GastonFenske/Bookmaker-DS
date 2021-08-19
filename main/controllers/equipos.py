from .. import db
from flask_restful import Resource
from main.models import EquipoModel
from flask import request, jsonify

class Equipo(Resource):
    def get(self, id):
        equipo = db.session.query(EquipoModel).get_or_404(id)
        try:
            return equipo.to_json()
        except:
            return '', 404

    def delete(self, id):
        equipo = db.session.query(EquipoModel).get_or_404(id)
        try:
            db.session.delete(equipo)
            db.session.commit()
            return '', 204
        except:
            return '', 404


class Equipos(Resource):

    def get(self):
        equipos = db.session.query(EquipoModel).all()

        return jsonify({
            'Equipos': [equipo.to_json() for equipo in equipos]
        })

    def post(self):

        equipo = EquipoModel.from_json(request.get_json())
        db.session.add(equipo)
        db.session.commit()
        return equipo.to_json(), 201