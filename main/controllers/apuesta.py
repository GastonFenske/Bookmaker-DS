from flask_restful import Resource
from flask import request
from main.services import PartidoService


class Apuesta(Resource):
    def get(self):
        return PartidoService.obtener_partidos_no_finalizados()