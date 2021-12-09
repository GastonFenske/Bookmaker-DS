from flask_restful import Resource
from flask import request
from main import services
from main.services import ApuestaService
from main.map import ApuestaSchema, apuesta_schema
from .. import db
from main.repositories import ApuestaRepositorio

apuesta_schema = ApuestaSchema()
repositorio_apuesta = ApuestaRepositorio()
apuesta_service = ApuestaService()

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
        services = ApuestaService()
        apuesta = apuesta_schema.load(request.get_json())
        #apuesta = repositorio_apuesta.create()
        #print(services.registrar_apuestas(apuesta))
        return services.agregar_apuesta(apuesta)
        return services.registrar_apuestas(apuesta)

    def get(self):
        return apuesta_schema.dump(repositorio_apuesta.find_wins(), many=True)
        