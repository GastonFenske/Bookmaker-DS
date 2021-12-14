from .. import db
from main.models import CuotaModel

class ValidateCuota():

    def validar_cuota(self, id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                cuota = db.session.query(CuotaModel).get(id)
                if cuota:
                    return function(*args, **kwargs)
                return 'Cuota no encontrada', 404
            return wrapper
        return decorator 