from main.models import EquipoModel
from .. import db

class ValidateEquipo():

    def validar_equipo(self, id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                #En estos decoradores pordiramos usar los repositorios tambien para conectarnos a la base de datos
                equipo = db.session.query(EquipoModel).get(id)
                if equipo:
                    return function(*args, **kwargs)
                return 'Equipo no encontrado', 404
            return wrapper
        return decorator
            