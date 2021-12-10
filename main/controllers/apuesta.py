from flask_restful import Resource
from flask import request
from main import services
from main.services import ApuestaService
from main.map import ApuestaSchema, apuesta_schema
from .. import db
from main.repositories import ApuestaRepositorio
from main.validate import ValidateApuesta
# from main.validate.validate_apuesta import validar_cliente

apuesta_schema = ApuestaSchema()
repositorio_apuesta = ApuestaRepositorio()
apuesta_service = ApuestaService()
validate_apuesta = ValidateApuesta()

class Apuesta(Resource):
    def get(self, id):
        """"""
        return apuesta_schema.dump(repositorio_apuesta.find_one(id))
        #return PartidoService.obtener_partidos_no_finalizados()


class Apuestas(Resource):
    # def post(self):
    #     """Metodo para crear una apuesta"""
    #     apuesta = apuesta_schema.load(request.get_json())
    #     db.session.add(apuesta)
    #     db.session.commit()
    #     return apuesta_schema.dump(apuesta)

    def post(self):
        apuesta = apuesta_schema.load(request.get_json())
        @validate_apuesta.validar_cliente(apuesta.cliente)
        @validate_apuesta.validar_partido(apuesta.partido)
        @validate_apuesta.validar_equipo(apuesta.equipo_ganador_id)
        @validate_apuesta.validar_monto(apuesta.monto)
        def validate_post():
            return apuesta_service.agregar_apuesta(apuesta)
            # return services.registrar_apuestas(apuesta)
        return validate_post()

    def get(self):
        return apuesta_schema.dump(repositorio_apuesta.find_wins(), many=True)        