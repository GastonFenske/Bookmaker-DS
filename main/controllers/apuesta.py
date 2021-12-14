from flask_restful import Resource
from flask import request
from main.services import ApuestaService
from main.map import ApuestaSchema, apuesta_schema
from main.repositories import ApuestaRepositorio
from main.validate import ValidateApuesta

apuesta_schema = ApuestaSchema()
repositorio_apuesta = ApuestaRepositorio()
apuesta_service = ApuestaService()
validate_apuesta = ValidateApuesta()

class Apuesta(Resource):
    #Falta validar que la apuesta exista
    def get(self, id):
        return apuesta_schema.dump(repositorio_apuesta.find_one(id))
        #return PartidoService.obtener_partidos_no_finalizados()

class Apuestas(Resource):
    def post(self):
        apuesta = apuesta_schema.load(request.get_json())
        @validate_apuesta.validar_apuesta(apuesta)
        def validate_post():
            return apuesta_schema.dump(apuesta_service.agregar_apuesta(apuesta))
            # return services.registrar_apuestas(apuesta)
        return validate_post()

    def get(self):
        return apuesta_schema.dump(repositorio_apuesta.find_wins(), many=True)        