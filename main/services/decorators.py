from .. import db
from main.models import EquipoModel, PartidoModel, ClienteModel, CuotaModel
from functools import wraps


def validar_apuesta(equipo_id, monto):
    def decorator(function):
        def wrapper(*args, **kwargs):
            equipo = db.session.query(EquipoModel).get(equipo_id)
            if equipo and monto >= 20.0:
                return function(*args, **kwargs)
            else:
                return 'La apuesta no ha sido validada', 401
        return wrapper
    return decorator

def validar_equipo(equipo_id: int):
    def decorator(function):
        def wrapper(*args, **kwargs):
            equipo = db.session.query(EquipoModel).get(equipo_id)
            if equipo:
                return function(*args, **kwargs)
            return 'Equipo no encontrado', 404
        return wrapper
    return decorator

def validar_equipo_pro(*ids):
    """Decorador para validar mas de un equipo"""
    def decorator(function):
        def wrapper(*args, **kwargs):
            for id in ids:
                equipo = db.session.query(EquipoModel).get(id)
                if not equipo:
                    return f'El equipo con el id: {id} no ha sido encontrado', 404
                    break
            return function(*args, **kwargs)
        return wrapper
    return decorator


def validar(param: int, model: db.Model):
    def decorator(function):
        def wrapper(*args, **kwargs):
            objeto = db.session.query(model).get(param)
            if objeto:
                return function(*args, **kwargs)
            return 'Conflict', 409
        return wrapper
    return decorator


def validar_monto(monto: float):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if monto >= 20.0:
                return function(*args, **kwargs)
            return 'Monto por abajo del minimo para apostar', 401
        return wrapper
    return decorator

def validar_partido(partido_id):
    def decorator(function):
        def wrapper(*args, **kwargs):
            partido = db.session.query(PartidoModel).get(partido_id)
            if partido and partido.finalizado != True:
                return function(*args, **kwargs)
            return 'No es posible apostar por ese partido', 404
        return wrapper
    return decorator

def validar_cliente(cliente_id):
    def decorator(function):
        def wrapper(*args, **kwargs):
            cliente = db.session.query(ClienteModel).get(cliente_id)
            if cliente:
                return function(*args, **kwargs)
            return 'Cliente no encontrado', 404
        return wrapper
    return decorator


def singleton(cls):
    instances = dict()
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper
