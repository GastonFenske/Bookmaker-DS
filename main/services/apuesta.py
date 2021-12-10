from main.models.cuota import Cuota
from .. import db
from main.models import ApuestaModel, EquipoModel, ClienteModel, PartidoModel, CuotaModel
from .command import Command, Tarea
from main.map import ApuestaSchema, apuesta_schema
from .decorators import validar_apuesta, validar_equipo, validar_monto, validar_partido, validar_cliente
from main.repositories import ApuestaRepositorio, CuotaRepositorio
from abc import ABC

apuesta_schema = ApuestaSchema()
apuesta_repositorio = ApuestaRepositorio()
cuota_repositorio = CuotaRepositorio()

class ApuestaService:
    def registrar_apuestas(self, apuesta):
        tarea = Tarea()
        # tarea.agregar(ValidarEquipo(apuesta.equipo_ganador_id))
        tarea.agregar(ValidarEquipo())
        # tarea.agregar(ValidarMontos())

        tarea.agregar(GuardarApuesta())

        orden_a_ejecutar = tarea.execute(apuesta)
        #print(orden_a_ejecutar, "[ORDEN A EJECUTAR]") 
        tarea.execute(apuesta)
        #return tarea.execute(apuesta)
        #return orden_a_ejecutar


    def agregar_apuesta(self, apuesta):
        # Habria traer la cuota desde el repositorio de cuota
        # cuota = db.session.query(CuotaModel).filter(CuotaModel.partido_id == apuesta.partido)[0]
        cuota = cuota_repositorio.find_one(apuesta)
        probabilidad = set_probabilidad(apuesta, cuota)
        apuesta.ganancia = apuesta.monto * probabilidad
        return apuesta_schema.dump(apuesta_repositorio.create(apuesta))


class ValidarEquipo(Command):
    def execute(self, param):
        print('Esta entrando a validar equipo')
        print(param, "[PARAMETRO: que deberia ser un id de equipos]")
        equipo = db.session.query(EquipoModel).get(param.equipo_ganador_id)
        print(equipo, "[EQUIPO]")
        if equipo:
            print('Aca no entra')
            return 'Unauthorized', 401 
            #return True
        else:
            print('Aca si')
            #return 'Hola'
            #return False 
            return 'Equipo no encontrado', 404

class ValidarMontos(Command):
    def execute(self, param):
        pass

class GuardarApuesta(Command):
    def execute(self, param):
        print('ESTA ENTRANDO A GUARDAR APUESTA')
        db.session.add(param)
        db.session.commit()
        return apuesta_schema.dump(param)

class EnviarMail(Command):
    def execute(self, param):
        pass






def validar_partido_local(objeto):
    partido_local = db.session.query(PartidoModel).filter((PartidoModel.equipo_local_id == objeto.equipo_ganador_id) & (PartidoModel.id == objeto.partido)).count()
    return True if partido_local != 0 else False

def set_probabilidad(objeto, cuota):
    if validar_partido_local(objeto):
        probabilidad_local = ProbabilidadLocal()
        probabilidad = probabilidad_local.calcular_probabilidad(cuota)
        return probabilidad
    probabilidad_visitante = ProbabilidadVisitante()
    probabilidad = probabilidad_visitante.calcular_probabilidad(cuota)
    return probabilidad

class ProbabilidadStrategy(ABC):
    def calcular_probabilidad(self, cuota):
        """Calcular probabilidad"""

class ProbabilidadLocal(ProbabilidadStrategy):
    def calcular_probabilidad(self, cuota):
        probabilidad = cuota.probabilidad_local
        return probabilidad

class ProbabilidadVisitante(ProbabilidadStrategy):
    def calcular_probabilidad(self, cuota):
        probabilidad = cuota.probabilidad_visitante
        return probabilidad