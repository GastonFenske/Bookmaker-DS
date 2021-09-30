from .. import db
from main.models import PartidoModel 

class PartidoService:
    def obtener_partidos_no_finalizados():
        partidos = db.session.query(PartidoModel).filter('finalizado' == False).all()
        return partidos