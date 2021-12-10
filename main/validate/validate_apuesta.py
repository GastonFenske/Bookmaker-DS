from .. import db
from main.models import EquipoModel, PartidoModel, ClienteModel, CuotaModel
from functools import wraps

#Strategy, un decorador mas general o algo ase
class ValidateApuesta():

    @staticmethod
    def validar_equipo(equipo_id: int):
        def decorator(function):
            def wrapper(*args, **kwargs):
                equipo = db.session.query(EquipoModel).get(equipo_id)
                if equipo:
                    return function(*args, **kwargs)
                return 'Equipo no encontrado', 404
            return wrapper
        return decorator

    @staticmethod
    def validar_monto(monto: float):
        def decorator(function):
            def wrapper(*args, **kwargs):
                if monto >= 20.0:
                    return function(*args, **kwargs)
                return 'Monto por abajo del minimo para apostar', 409
            return wrapper
        return decorator

    @staticmethod
    def validar_partido(partido_id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                partido = db.session.query(PartidoModel).get(partido_id)
                if partido and partido.finalizado != True:
                    return function(*args, **kwargs)
                return 'Ese partido no existe o ha finalizado', 404
            return wrapper
        return decorator
    
    @staticmethod
    def validar_cliente(cliente_id):
        def decorator(function):
            @wraps(function)
            def wrapper(*args, **kwargs):
                cliente = db.session.query(ClienteModel).get(cliente_id)
                if cliente:
                    return function(*args, **kwargs)
                return 'Cliente no encontrado', 404
            return wrapper
        return decorator




