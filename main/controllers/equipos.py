from .. import db
from flask_restful import Resource
from main.models import EquipoModel
from flask import request, jsonify
from main.map import EquipoSchema
import logging

equipo_schema = EquipoSchema()
logger = logging.getLogger(__name__)

class Equipo():
    pass





# class Equipo(Resource):
#     def get(self, id):
#         equipo = db.session.query(EquipoModel).get_or_404(id)
#         try:
#             return equipo_schema.dump(equipo), 201
#         except:
#             return '', 404

#     def delete(self, id):
#         equipo = db.session.query(EquipoModel).get_or_404(id)
#         try:
#             db.session.delete(equipo)
#             db.session.commit()
#             return '', 204
#         except:
#             return '', 404

#     def put(self, id):
#         equipo = db.session.query(EquipoModel).get_or_404(id)
#         data = request.get_json().items()
#         for key, value in data:
#             setattr(equipo, key, value)
#         try:
#             db.session.add(equipo)  
#             db.session.query()
#             return equipo_schema.dump(equipo), 201
#         except:
#             return '', 404

# class Equipos(Resource):

#     def get(self):
#         equipos = db.session.query(EquipoModel).all()
#         return equipo_schema.dump(equipos, many=True)

#     def post(self):
#         equipo = equipo_schema.load(request.get_json())
#         db.session.add(equipo)
#         db.session.commit()
#         return equipo_schema.dump(equipo), 201