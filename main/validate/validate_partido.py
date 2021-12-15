from main.services.partidos import PartidoService

service = PartidoService()

class ValidatePartido():

    def validar_partido(self, id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                partido = service.obtener_partido_por_id(id)
                if partido:
                    return function(*args, **kwargs)
                return 'Ese partido no existe', 404
            return wrapper
        return decorator


    def validar_partido_finalizado(self, id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                partido = service.obtener_partido_por_id(id)
                if partido.finalizado:
                    return 'Partido finalizado', 404
                return function(*args, **kwargs)
            return wrapper
        return decorator 


