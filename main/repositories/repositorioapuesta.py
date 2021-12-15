from sqlalchemy.sql.elements import or_
from .. import db
from main.models import ApuestaModel, PartidoModel, CuotaModel
from .repositoriobase import Create, Read
from flask import request
from main.utils import SingletonPattern
from sqlalchemy import or_

singleton_pattern = SingletonPattern()

@singleton_pattern.singleton
class ApuestaRepositorio(Create, Read): 

    def __init__(self):
        self.__modelo = ApuestaModel

    @property
    def modelo(self):
        return self.__modelo

    def find_one(self, id):
        objeto = db.session.query(self.modelo).get(id)
        return objeto

    def find_wins(self):
        objetos = db.session.query(self.modelo).filter(or_(self.modelo.equipo_ganador_id == PartidoModel.ganador_id, self.modelo.equipo_ganador_id == None) & (PartidoModel.finalizado == True))
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'cliente_id':
                    objetos = objetos.filter(self.modelo.cliente_id == value)
        return objetos

    def find_all(self):
        objetos = db.session.query(self.modelo)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'cliente_id':
                    objetos = objetos.filter(self.modelo.cliente_id == value)    
        return objetos

    def create(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto    

    

