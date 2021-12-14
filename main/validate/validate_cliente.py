from .. import db
from main.models import ClienteModel

class ValidateCliente():

    def __init__(self):
        self.__modelo = ClienteModel
    
    @property
    def modelo(self):
        return self.__modelo

    def validar_cliente(self, id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                cliente = db.session.query(self.modelo).get(id)
                if cliente:
                    return function(*args, **kwargs)
                return 'Cliente no encontrado', 404
            return wrapper
        return decorator