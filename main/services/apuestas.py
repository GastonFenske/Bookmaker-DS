from flask_restful import Resource
from flask import request
from main.services import PartidoService

class Apuestas(Resource):
    def get(self):
        services = PartidoService()
        return services.obtener_partidos_no_finalizados() 