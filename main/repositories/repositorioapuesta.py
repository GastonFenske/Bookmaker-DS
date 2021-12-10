from main.models.partido import Partido
from flask.signals import request_started
from .. import db
from main.models import ApuestaModel, PartidoModel, CuotaModel
from .repositoriobase import Create, Read
from flask import request
# from main.services.decorators import singleton, validar_cuota
from abc import ABC, abstractmethod
from main.utils import SingletonPattern

singleton_pattern = SingletonPattern()

@singleton_pattern.singleton
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


    def find_all(self):
        """"""
        objetos = db.session.query(self.modelo)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'cliente':
                    objetos = objetos.filter(self.modelo.cliente == value)    
        return objetos


    def create(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto    

    

