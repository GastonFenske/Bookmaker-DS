from main.map import ApuestaSchema, apuesta_schema
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
        if validate_partido.validar_partido_visitante(objeto):
            probabilidad_visitante = ProbabilidadVisitante()
            probabilidad = probabilidad_visitante.calcular_probabilidad(cuota)
            return probabilidad
        probabilidad_empate = ProbabilidadEmpate()
        probabilidad = probabilidad_empate.calcular_probabilidad(cuota)
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

class ProbabilidadEmpate(ProbabilidadStrategy):
    def calcular_probabilidad(self, cuota):
        probabilidad = cuota.probabilidad_empate
        return probabilidad