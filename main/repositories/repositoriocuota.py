from .repositoriobase import Create, Read
from main.models import CuotaModel
from .. import db

class CuotaRepositorio(Read):
    def find_one(self, objeto):
        cuota = db.session.query(CuotaModel).filter(CuotaModel.partido_id == objeto.partido)[0]
        return cuota

    def find_all(self):
        return super().find_all()
