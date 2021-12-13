from main.models import PartidoModel
from .. import db

class ValidatePartido():


    def validar_partido(self, partido_id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                partido = db.session.query(PartidoModel).get(partido_id)
                #Podria validar que exista y otra funcion que valide si esta finalizado
                if partido:
                    return function(*args, **kwargs)
                return 'Ese partido no existe', 404
            return wrapper
        return decorator

    def validar_partido_finalizado(self, id):
        """"""

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
