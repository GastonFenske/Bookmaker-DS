from main.models import PartidoModel
from .. import db

class ValidatePartido():


    #quizas aca tambien se puede colocar un strategy
    def validar_partido_local(self, objeto):
        partido_local = db.session.query(PartidoModel).filter((PartidoModel.equipo_local_id == objeto.equipo_ganador_id) & (PartidoModel.id == objeto.partido)).count()
        return True if partido_local != 0 else False

    def validar_partido_visitante(self, objeto):
        partido_visitante = db.session.query(PartidoModel).filter((PartidoModel.equipo_visitante_id == objeto.equipo_ganador_id) & (PartidoModel.id == objeto.partido)).count()
        return True if partido_visitante != 0 else False

    def validar_partido_empate(self, objeto):
        """"""
        # partido_empate = db.session.query(PartidoModel).filter(PartidoModel.equipo_local_id == objeto.partido )
