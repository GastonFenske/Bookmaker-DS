from main.models.partido import Partido
from flask.signals import request_started
from .. import db
from main.models import ApuestaModel, PartidoModel, CuotaModel
from .repositoriobase import Create, Read
from flask import request
# from main.services.decorators import singleton, validar_cuota
from abc import ABC, abstractmethod


def singleton(cls):
    instances = dict()
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class ApuestaRepositorio(Create, Read): 

    def __init__(self):
        self.__modelo = ApuestaModel

    @property
    def modelo(self):
        return self.__modelo

    def find_one(self, id):
        objeto = db.session.query(self.modelo).get_or_404(id)
        return objeto


    def find_wins(self):
        objetos = db.session.query(self.modelo).filter(self.modelo.equipo_ganador_id == PartidoModel.ganador)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'cliente':
                    objetos = objetos.filter(self.modelo.cliente == value)
        return objetos

        # objetos = db.session.query(self.modelo).filter(self.modelo.cliente == 99).filter(self.modelo.equipo_ganador_id == PartidoModel.ganador)

        # if request.get_json():
        #     filters = request.get_json().items()
        #     for key, value in filters:
        #         if key == 'cliente':
        #             objetos = objetos.filter(self.modelo.cliente == value)
        return objetos

    def find_all(self):
        """"""
        objetos = db.session.query(self.modelo)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'cliente':
                    objetos = objetos.filter(self.modelo.cliente == value)    
        return objetos

    # def find_by_client(self, client_id):
    #     objeto = db.session.query(self.modelo)
    #     objeto = objeto.filter(self.modelo.cliente == client_id)
    #     return objeto

    def create(self, objeto):
        # Habria traer la cuota desde el repositorio de cuota
        # cuota = db.session.query(CuotaModel).filter(CuotaModel.partido_id == objeto.partido)[0]

        # probabilidad = set_probabilidad(objeto, cuota)
        # objeto.ganancia = objeto.monto * probabilidad
        db.session.add(objeto)
        db.session.commit()
        return objeto    

def validar_partido_local(objeto):
    partido_local = db.session.query(PartidoModel).filter((PartidoModel.equipo_local_id == objeto.equipo_ganador_id) & (PartidoModel.id == objeto.partido)).count()
    return True if partido_local != 0 else False

def set_probabilidad(objeto, cuota):
    if validar_partido_local(objeto):
        probabilidad_local = ProbabilidadLocal()
        probabilidad = probabilidad_local.calcular_probabilidad(cuota)
        return probabilidad
    probabilidad_visitante = ProbabilidadVisitante()
    probabilidad = probabilidad_visitante.calcular_probabilidad(cuota)
    return probabilidad


class ProbabilidadStrategy(ABC):
    def calcular_probabilidad(self, cuota):
        """Calcular probabilidad"""

class ProbabilidadLocal(ProbabilidadStrategy):
    def calcular_probabilidad(self, cuota):
        probabilidad = cuota.probabilidad_local
        return probabilidad

class ProbabilidadVisitante(ProbabilidadStrategy):
    def calcular_probabilidad(self, cuota):
        probabilidad = cuota.probabilidad_visitante
        return probabilidad
    

