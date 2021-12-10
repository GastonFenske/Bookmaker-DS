from main.models.cuota import Cuota
from .. import db
from main.models import ApuestaModel, EquipoModel, ClienteModel, PartidoModel, CuotaModel
from .command import Command, Tarea
from main.map import ApuestaSchema, apuesta_schema
from .decorators import validar_apuesta, validar_equipo, validar_monto, validar_partido, validar_cliente
from main.repositories import ApuestaRepositorio, CuotaRepositorio
from abc import ABC
from main.validate import ValidatePartido

apuesta_schema = ApuestaSchema()
apuesta_repositorio = ApuestaRepositorio()
cuota_repositorio = CuotaRepositorio()
validate_partido = ValidatePartido()

class ApuestaService:

    def agregar_apuesta(self, apuesta):
        cuota = cuota_repositorio.find_one(apuesta)
        probabilidad = self.set_probabilidad(apuesta, cuota)
        apuesta.ganancia = apuesta.monto * probabilidad
        return apuesta_schema.dump(apuesta_repositorio.create(apuesta))

    def set_probabilidad(self, objeto, cuota):
        if validate_partido.validar_partido_local(objeto):
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