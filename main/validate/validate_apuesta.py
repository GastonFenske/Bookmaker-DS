from operator import or_
from .. import db
from main.models import EquipoModel, PartidoModel, ClienteModel, CuotaModel
from functools import wraps
from sqlalchemy import or_

#Strategy, un decorador mas general o algo ase
class ValidateApuesta():

    def validar_equipo(self, objeto):
        def decorator(function):
            def wrapper(*args, **kwargs):
                equipos = db.session.query(EquipoModel).filter(or_(EquipoModel.id == PartidoModel.equipo_local_id, EquipoModel.id == PartidoModel.equipo_visitante_id) & (PartidoModel.id == objeto.partido)).all()
                equipos = [e.id for e in equipos]
                if objeto.equipo_ganador_id in equipos or objeto.equipo_ganador_id == None:
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
                @self.validar_equipo(objeto)
                @self.validar_monto(objeto.monto)
                @self.validar_partido(objeto.partido)
                def add():
                    return function(*args, **kwargs)
                return add()
            return wrapper
        return decorator




