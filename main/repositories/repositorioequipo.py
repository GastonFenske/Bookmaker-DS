from .. import db
from main.models import EquipoModel
from .repositoriobase import Create, Read, Update, Delete

class EquipoRepositorio(Create, Read, Update, Delete):

    def __init__(self):
        self.__modelo = EquipoModel
    
    @property
    def modelo(self):
        return self.__modelo

    def find_all(self):
        objetos = db.session.query(self.modelo).all()
        return objetos

    def find_one(self, id):
        objeto = db.session.query(self.modelo).get(id)
        return objeto

    def create(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto

    def delete(self, id):
        objeto = db.session.query(self.modelo).get(id)
        return self.__soft_delete(objeto)

    def update(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto


    def __soft_delete(self, objeto):
        objeto.activado = False
        return self.update(objeto)
