from flask_restful import Resource
from main.map import EquipoSchema
from main.services import EquipoService
import logging
from main.validate import ValidateEquipo
from flask import request

equipo_schema = EquipoSchema()
equipo_service = EquipoService()
logger = logging.getLogger(__name__)

validate_equipo = ValidateEquipo()

class Equipos(Resource):

    def get(self):
        #Aca podriamos filtrar por pais o algun otro tipo de filtrado
        return equipo_schema.dump(equipo_service.obtener_equipos(), many=True)

    def post(self):
        equipo = equipo_schema.load(request.get_json())
        return equipo_schema.dump(equipo_service.agregar_equipo(equipo))

class Equipo(Resource):

    def get(self, id):
        @validate_equipo.validar_equipos(id)
        def validated():
            return equipo_schema.dump(equipo_service.obtener_equipo_por_id(id))
        return validated()

    #Esto quizas se puede mejorar con lamda functions
    #Mejorar esto con lamda functions
    def delete(self, id):
        @validate_equipo.validar_equipos(id)
        def validated():
            return equipo_schema.dump(equipo_service.eliminar_equipo(id))
        return validated()

    def put(self, id):
        @validate_equipo.validar_equipos(id)
        def validated():
            equipo = request.get_json()
            return equipo_schema.dump(equipo_service.actualizar_equipo(id, equipo))
        return validated()
