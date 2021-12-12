from .. import db
from main.models import EquipoModel, PartidoModel, ClienteModel, CuotaModel
from functools import wraps

#Strategy, un decorador mas general o algo ase
class ValidateApuesta():

    def validar_equipo(self, equipo_id: int):
        def decorator(function):
            def wrapper(*args, **kwargs):
                equipo = db.session.query(EquipoModel).get(equipo_id)
                if equipo or equipo_id == None:
                    return function(*args, **kwargs)
                return 'Equipo no encontrado', 404
            return wrapper
        return decorator

    def validar_monto(self, monto: float):
        def decorator(function):
            def wrapper(*args, **kwargs):
                if monto >= 20.0:
                    return function(*args, **kwargs)
                return 'Monto por abajo del minimo para apostar', 409
            return wrapper
        return decorator

    def validar_partido(self, partido_id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                partido = db.session.query(PartidoModel).get(partido_id)
                #Podria validar que exista y otra funcion que valide si esta finalizado
                if partido and partido.finalizado != True:
                    return function(*args, **kwargs)
                return 'Ese partido no existe o ha finalizado', 404
            return wrapper
        return decorator
    
    def validar_cliente(self, cliente_id):
        def decorator(function):
            @wraps(function)
            def wrapper(*args, **kwargs):
                cliente = db.session.query(ClienteModel).get(cliente_id)
                if cliente:
                    return function(*args, **kwargs)
                return 'Cliente no encontrado', 404
            return wrapper
        return decorator 

    def validar_apuesta(self, objeto):
        def decorator(function):
            def wrapper(*args, **kwargs):
                @self.validar_cliente(objeto.cliente)
                @self.validar_equipo(objeto.equipo_ganador_id)
                @self.validar_monto(objeto.monto)
                @self.validar_partido(objeto.partido)
                def add():
                    return function(*args, **kwargs)
                return add()
            return wrapper
        return decorator




