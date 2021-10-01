from .. import db
from main.models import PartidoModel
from .repositoriobase import Create, Read, Delete, Update
import logging

logger = logging.getLogger(__name__)


class PartidoRepositorio(Create, Read, Delete, Update):

    def __init__(self):
        self.__modelo = PartidoModel

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
        try:
            objeto = db.session.query(self.modelo).get_or_404(id)
            db.session.delete(objeto)
            db.session.commit()
        except Exception as error:
            logger.error(f'No se pudo borrar %s {id}')
            db.session.rollback()

