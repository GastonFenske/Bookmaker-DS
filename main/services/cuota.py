from main.repositories.repositoriocuota import CuotaRepositorio
from main.services.partidos import PartidoService
from main.services.equipo import EquipoService
from math import cos

repositorio = CuotaRepositorio()
partido_service = PartidoService()
equipo_service = EquipoService()

class CuotaService:

    def obtener_cuotas(self):
        return repositorio.find_all()

    def obtener_cuota(self, id):
        return repositorio.find_one(id)

    def agregar_cuota(self, cuota):
        self.aplicar_cuotas(cuota)
        return repositorio.create(cuota)

    def aplicar_cuotas(self, cuota) -> None:
        partido = partido_service.obtener_partido_por_id(cuota.partido_id)
        visitante = equipo_service.obtener_equipo_por_id(partido.equipo_visitante_id)
        local = equipo_service.obtener_equipo_por_id(partido.equipo_local_id)
        
        cuota.cuota_local = self.calcular_cuota(local.puntaje)
        cuota.cuota_visitante = self.calcular_cuota(visitante.puntaje)
        cuota.cuota_empate = self.calcular_cuota(self.calcular_empate(local.puntaje, visitante.puntaje))

    def calcular_base(self):
        return equipo_service.obtener_puntaje_mas_alto()
    
    def calcular_probabilidad(self, puntos):
        return puntos/self.calcular_base()

    def calcular_empate(self, puntos_local, puntos_visitante):
        return abs(puntos_local - puntos_visitante)

    def calcular_cuota(self, puntos):
        cuota_calculada = cos(self.calcular_probabilidad(puntos))
        cuota_calculada = (cuota_calculada * 10) - 4
        return round(cuota_calculada, 2)




        

