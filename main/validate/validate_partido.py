from main.models import PartidoModel
from .. import db

class ValidatePartido():

    def __init__(self):
        self.__modelo = PartidoModel
    
    @property
    def modelo(self):
        return self.__modelo


    def validar_partido(self, id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                partido = db.session.query(self.modelo).get(id)
                #Podria validar que exista y otra funcion que valide si esta finalizado
                if partido:
                    return function(*args, **kwargs)
                return 'Ese partido no existe', 404
            return wrapper
        return decorator


    def validar_partido_finalizado(self, id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                partido = db.session.query(self.modelo).get(id)
                if partido.finalizado:
                    return 'Partido finalizado', 404
                return function(*args, **kwargs)
            return wrapper
        return decorator 

    #quizas aca tambien se puede colocar un strategy
    def validar_partido_local(self, objeto):
        partido_local = db.session.query(self.modelo).filter((self.modelo.equipo_local_id == objeto.equipo_ganador_id) & (self.modelo.id == objeto.partido)).count()
        return True if partido_local != 0 else False

    def validar_partido_visitante(self, objeto):
        partido_visitante = db.session.query(self.modelo).filter((self.modelo.equipo_visitante_id == objeto.equipo_ganador_id) & (self.modelo.id == objeto.partido)).count()
        return True if partido_visitante != 0 else False

    def validar_partido_empate(self, objeto):
        """"""
        # partido_empate = db.session.query(PartidoModel).filter(PartidoModel.equipo_local_id == objeto.partido )
