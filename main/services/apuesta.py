from main.map import ApuestaSchema
from main.repositories import ApuestaRepositorio, CuotaRepositorio
from abc import ABC
from main.validate.validate_partido import ValidatePartido

apuesta_schema = ApuestaSchema()
apuesta_repositorio = ApuestaRepositorio()
cuota_repositorio = CuotaRepositorio()
validate_partido = ValidatePartido()

class ApuestaService:

    def agregar_apuesta(self, apuesta):
        cuota = cuota_repositorio.find_by_partido(apuesta)
        probabilidad = self.set_cuota(apuesta, cuota)
        apuesta.ganancia = round(apuesta.monto * probabilidad, 2)
        return apuesta_repositorio.create(apuesta)

    def set_cuota(self, objeto, cuota):
        if validate_partido.validar_partido_local(objeto):
            cuota_local = CuotaLocal()
            probabilidad = cuota_local.calcular_cuota(cuota)
            return probabilidad
        if validate_partido.validar_partido_visitante(objeto):
            cuota_visitante = CuotaVisitante()
            probabilidad = cuota_visitante.calcular_cuota(cuota)
            return probabilidad
        cuota_empate = CuotaEmpate()
        probabilidad = cuota_empate.calcular_cuota(cuota)
        return probabilidad

class CuotaStrategy(ABC):
    def calcular_cuota(self, cuota):
        """Calcular probabilidad"""

class CuotaLocal(CuotaStrategy):
    def calcular_cuota(self, cuota):
        probabilidad = cuota.cuota_local
        return probabilidad

class CuotaVisitante(CuotaStrategy):
    def calcular_cuota(self, cuota):
        probabilidad = cuota.cuota_visitante
        return probabilidad

class CuotaEmpate(CuotaStrategy):
    def calcular_cuota(self, cuota):
        probabilidad = cuota.cuota_empate
        return probabilidad