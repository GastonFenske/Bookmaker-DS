from main.models import EquipoModel
from .. import db

class ValidateEquipo():

    def __init__(self):
        self.__modelo = EquipoModel
    
    @property
    def modelo(self):
        return self.__modelo

    def validar_equipo(self, *ids):
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
            