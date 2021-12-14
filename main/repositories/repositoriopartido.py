from .. import db
from main.models import PartidoModel
from .repositoriobase import Create, Read, Delete, Update
import logging
from .repositoriocuota import CuotaRepositorio
# from main.services import CuotaService
from main.map import CuotaSchema

# from main.controllers.cuota import aplicar_probabilidades

logger = logging.getLogger(__name__)

cuota_repositorio = CuotaRepositorio()
cuota_schema = CuotaSchema()
# cuota_service = CuotaService()

class PartidoRepositorio(Create, Read, Delete, Update):

    def __init__(self):
        self.__modelo = PartidoModel

    @property
    def modelo(self):
        return self.__modelo

    def find_one(self, id):
        objeto = db.session.query(self.modelo).get(id)
        return objeto

    def find_all(self):
        objetos = db.session.query(self.modelo).all()
        return objetos

    def create(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        #Aca vamos a crear la cuota automaticamente
        # json = {
        #     "partido_id": objeto.id
        # }
        # cuota = cuota_schema.load(json)
        # # aplicar_probabilidades(cuota)
        return objeto

    def update(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto

    def delete(self, id):
        partido = db.session.query(self.modelo).get(id)
        db.session.delete(partido)
        db.session.commit()
        return partido

