from flask_restful import Resource
from flask import request
from main.map import CuotaSchema, couta_schema
from .. import db
from main.models import PartidoModel, EquipoModel
from math import cos
from main.repositories import CuotaRepositorio

cuota_schema = CuotaSchema()
cuota_repositorio = CuotaRepositorio()

class Cuota(Resource):
    """"""


class Cuotas(Resource):
    """"""
    def post(self):
        cuota = cuota_schema.load(request.get_json())
        aplicar_probabilidades(cuota)
        # db.session.add(cuota)
        # db.session.commit()
        return cuota_schema.dump(cuota_repositorio.create(cuota))

    
def aplicar_probabilidades(cuota) -> None:
    cuota.probabilidad_local = None
    cuota.probabilidad_visitante = None
    cuota.probabilidad_empate = None

    partido_id = cuota.partido_id
    partido = db.session.query(PartidoModel).get(partido_id)
    equipo_visitante = db.session.query(EquipoModel).get(partido.equipo_visitante_id)
    equipo_local = db.session.query(EquipoModel).get(partido.equipo_local_id)
    puntos_visitante = equipo_visitante.puntaje
    puntos_local = equipo_local.puntaje

    equipos = db.session.query(EquipoModel).all()
    puntajes = [e.puntaje for e in equipos]
    puntajes.sort()
    puntaje_mas_alto = puntajes[-1] 

    def calcular_probabilidad(puntos):
        return puntos/puntaje_mas_alto

    if puntos_local >= puntos_visitante:
        empate = puntos_local - puntos_visitante
    else:
        empate = (puntos_local - puntos_visitante) * -1 

    cuota.probabilidad_local = round((cos(calcular_probabilidad(puntos_local)) *10 - 4), 2)
    cuota.probabilidad_visitante = round((cos(calcular_probabilidad(puntos_visitante)) *10 - 4), 2)
    cuota.probabilidad_empate = round((cos(calcular_probabilidad(float(empate))) *10 - 4), 2)




