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
        objeto = db.session.query(self.modelo).get_or_404(id)
        return objeto

    def create(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto

    #La clase abstracta tiene problemas si no se crean sus metodos abstractos
    def delete(self, id):
        objeto = db.session.query(self.modelo).get_or_404(id)
        # db.session.delete(objeto)
        # db.session.commit()
        self.__soft_delete(objeto, id)

    def update(self, data, id):
        objeto = db.session.query(self.modelo).get_or_404(id)
        for key, value in data:
            setattr(objeto, key, value)
        db.session.add(objeto)
        db.session.commit()
        return objeto