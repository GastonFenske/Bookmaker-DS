from main.services.cliente import ClienteService

service = ClienteService()
class ValidateCliente():

    def validar_cliente(self, id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                if service.obtener_cliente(id):
                    return function(*args, **kwargs)
                return 'Cliente no encontrado', 404
            return wrapper
        return decorator