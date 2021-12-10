from main.models import PartidoModel
from .. import db

class ValidatePartido():


    def validar_partido_local(self, objeto):
        partido_local = db.session.query(PartidoModel).filter((PartidoModel.equipo_local_id == objeto.equipo_ganador_id) & (PartidoModel.id == objeto.partido)).count()
        return True if partido_local != 0 else False
