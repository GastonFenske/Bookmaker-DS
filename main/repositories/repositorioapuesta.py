from .. import db
from main.models import ApuestaModel
from .repositoriobase import Create, Read



class ApuestaRepositorio(Create, Read): 

    def __init__(self):
        self.__modelo = ApuestaModel

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

    

