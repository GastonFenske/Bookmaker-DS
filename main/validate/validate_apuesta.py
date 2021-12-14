# from .validate_equipo import ValidateEquipo
# from .validate_partido import ValidatePartido
# from .validate_cliente import ValidateCliente
from main.models import ApuestaModel
from .. import db
# from main.services.apuesta import ApuestaService

# validate_equipo = ValidateEquipo()
# validate_partido = ValidatePartido()
# validate_cliente = ValidateCliente()

#Strategy, un decorador mas general o algo ase
class ValidateApuesta():

    def __init__(self):
        self.__monto_minimo = 20.0
        self.__modelo = ApuestaModel
    
    @property
    def modelo(self):
        return self.__modelo

    @property
    def monto_minimo(self):
        return self.__monto_minimo

    def validar_monto(self, monto: float):
        def decorator(function):
            def wrapper(*args, **kwargs):
                if monto >= self.monto_minimo:
                    return function(*args, **kwargs)
                return 'Monto por abajo del minimo para apostar', 409
            return wrapper
        return decorator

    def validar_apuesta(self, objeto):
        def decorator(function):
            def wrapper(*args, **kwargs):
                @validate_cliente.validar_cliente(objeto.cliente)
                @validate_equipo.validar_equipo(objeto.equipo_ganador_id)
                @self.validar_monto(objeto.monto)
                @validate_partido.validar_partido(objeto.partido)
                @validate_partido.validar_partido_finalizado(objeto.partido)
                def add():
                    return function(*args, **kwargs)
                return add()
            return wrapper
        return decorator

    def validar_apuesta_existe(self, id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                apuesta = db.session.query(self.modelo).get(id)
                if apuesta:
                    return function(*args, **kwargs)
                return 'Apuesta no encontrada', 404
            return wrapper
        return decorator




