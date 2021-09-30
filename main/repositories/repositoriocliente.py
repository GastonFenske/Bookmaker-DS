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
        objeto = db.session.query(self.modelo).get_or_404(id)
        return objeto

    def find_all(self):
        objetos = db.session.query(self.modelo).all()
        return objetos

    def create(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto

    def update(self, data, id):
        objeto = db.session.query(self.modelo).get_or_404(id)
        for key, value in data:
            setattr(objeto, key, value)
        db.session.add(objeto)
        db.session.commit()
        return objeto

    def delete(self, id):
        objeto = db.session.query(self.modelo).get_or_404(id)
        db.session.delete(objeto)
        db.session.commit()

    def __soft_delete(self, objeto):
        objeto.activado = False #
        self.update(objeto, id)

