from .. import db
from flask_restful import Resource
from flask import request
from main.map import PartidoSchema
from main.repositories import PartidoRepositorio
from main.services import PartidoService
from main.validate import ValidatePartido
from main.validate import ValidateEquipo

partido_schema = PartidoSchema()
partido_repositorio = PartidoRepositorio()
service = PartidoService()
validate_partido = ValidatePartido()
validate_equipo = ValidateEquipo()


class Partido(Resource):
    def get(self, id):
        @validate_partido.validar_partido(id)
        def validated():
            return partido_schema.dump(service.obtener_partido_por_id(id))
        return validated()


    def delete(self, id):
        @validate_partido.validar_partido(id)
        def validated():
            return partido_schema.dump(service.eliminar_partido(id))
        return validated()

    def put(self, id):
        @validate_partido.validar_partido(id)
        def validated():
            data = request.get_json()
            return partido_schema.dump(service.actualizar_partido(id, data))
        return validated()

class Partidos(Resource):

    def get(self):
        return partido_schema.dump(service.obtener_partidos(), many=True)


    def post(self):
        partido = partido_schema.load(request.get_json())
        @validate_equipo.validar_equipos(partido.equipo_local_id, partido.equipo_visitante_id)
        def validated():
            return partido_schema.dump(service.agregar_partido(partido))
        return validated()

