from .repositoriobase import Create, Read
from main.models import CuotaModel
from .. import db


class CuotaRepositorio(Read, Create):

    def __init__(self):
        self.__modelo = CuotaModel
    
    @property
    def modelo(self):
        return self.__modelo

    def find_one(self, id):
        cuota = db.session.query(self.modelo).get(id)
        return cuota

    def find_by_partido(self, objeto):
        cuota = db.session.query(self.modelo).filter(self.modelo.partido_id == objeto.partido_id)[0]
        return cuota

    def find_all(self):
        cuotas = db.session.query(self.modelo).all()
        return cuotas

    def create(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto

    
