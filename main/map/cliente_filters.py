from main.models.cliente import Cliente
from main.models import ClienteModel

class ClienteFilters():
    
    def __init__(self, cliente):
        self.__cliente = cliente
        self.__filters = {
            "id": self.__id_filter,
            "nombre": self.__nombre_filter,
            "apellido": self.__apellido_filter,
            "email": self.__email_filter
        }

    def __id_filter(self, value):
        return self.__cliente.filter(ClienteModel.id == int(value))

    def __nombre_filter(self, value):
        return self.__cliente.filter(ClienteModel.nombre.like(f'%{value}%'))

    def __apellido_filter(self, value):
        return self.__cliente.filter(ClienteModel.apellido.like(f'%{value}%'))

    def __email_filter(self, value):
        return self.__cliente.filter(ClienteModel.email.like(f'%{value}%'))

    def filter(self, key, value):
        return self.__filters[key](value)
