from .. import db
from main.models import ClienteModel
from .repositoriobase import Create, Read, Delete, Update 


class ClienteRepositorio(Create, Read, Delete, Update):

    def __init__(self):
        self.__modelo = ClienteModel

    @property
    def modelo(self):
        return self.__modelo

    def find_one(self, id):
        objeto = db.session.query(self.modelo).get(id)
        return objeto

    def find_all(self):
        objetos = db.session.query(self.modelo).filter(self.activado == True).all()
        return objetos

    def create(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto

    def update(self, data, id):
        objeto = db.session.query(self.modelo).get(id)
        for key, value in data:
            setattr(objeto, key, value)
        db.session.add(objeto)
        db.session.commit()
        return objeto

    def delete(self, id):
        objeto = db.session.query(self.modelo).get(id)
        self.soft_delete(objeto, id)

    def __soft_delete(self, objeto, id):
        objeto.activado = False 
        self.update(objeto, id)

    def soft_delete(self, objeto, id):
        return self.__soft_delete(objeto, id)
    

