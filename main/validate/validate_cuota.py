from main.services.cuota import CuotaService

service = CuotaService()

class ValidateCuota():

    def validar_cuota(self, id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                cuota = service.obtener_cuota(id)
                if cuota:
                    return function(*args, **kwargs)
                return 'Cuota no encontrada', 404
            return wrapper
        return decorator 