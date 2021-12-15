from flask_restful import Resource
from flask import request
from main.services import ApuestaService
from main.map import ApuestaSchema
from main.repositories import ApuestaRepositorio
from main.validate import ValidateApuesta, ValidatePartido, ValidateEquipo

apuesta_schema = ApuestaSchema()
repositorio_apuesta = ApuestaRepositorio()
service = ApuestaService()
validate_apuesta = ValidateApuesta()
validate_partido = ValidatePartido()
validate_equipo = ValidateEquipo()

class Apuesta(Resource):
    def get(self, id):
        @validate_apuesta.validar_apuesta_existe(id)
        def validated():
            return apuesta_schema.dump(service.obtener_apuesta_por_id(id))
        return validated()


class Apuestas(Resource):
    def post(self):
        apuesta = apuesta_schema.load(request.get_json())
        @validate_apuesta.validar_apuesta(apuesta)
        def validate_post():
            local = validate_equipo.validar_equipo_local(apuesta)
            visitante = validate_equipo.validar_equipo_visitante(apuesta)
            return apuesta_schema.dump(service.agregar_apuesta(apuesta, local=local, visitante=visitante))
        return validate_post()

    def get(self):
        return apuesta_schema.dump(service.obtener_apuestas(), many=True)   

class ApuestasGanadas(Resource):
    def get(self):
        return apuesta_schema.dump(service.obtener_apuestas_ganadas(), many=True)

class ApuestaGanada(Resource):
    pass