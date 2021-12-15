from main.models import EquipoModel, PartidoModel
from .. import db
from operator import or_

class ValidateEquipo():

    def __init__(self):
        self.__modelo = EquipoModel
    
    @property
    def modelo(self):
        return self.__modelo

    def validar_equipos(self, *ids):
        """Decorador para validar mas de un equipo"""
        def decorator(function):
            def wrapper(*args, **kwargs):
                for id in ids:
                    equipo = db.session.query(self.modelo).get(id)
                    if not equipo:
                        return f'El equipo con el id: {id} no ha sido encontrado', 404
                        break
                return function(*args, **kwargs)
            return wrapper
        return decorator
    
    def validar_equipo(self, objeto):
        def decorator(function):
            def wrapper(*args, **kwargs):
                equipos = db.session.query(EquipoModel).filter(or_(EquipoModel.id == PartidoModel.equipo_local_id, EquipoModel.id == PartidoModel.equipo_visitante_id) & (PartidoModel.id == objeto.partido_id)).all()
                equipos = [e.id for e in equipos]
                if objeto.equipo_ganador_id in equipos or objeto.equipo_ganador_id == None:
                    return function(*args, **kwargs)
                return 'Equipo no encontrado en este partido', 404
            return wrapper
        return decorator
            