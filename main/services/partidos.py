# from .. import db
# from main.models import PartidoModel
from main.repositories.repositoriopartido import PartidoRepositorio
from main.map import PartidoSchema
# from .decorators import validar_equipo
# from .cuota import CuotaService
# from main.services import CuotaService
# from . import CuotaService
# from main.services.cuota import CuotaService
# from .cuota import CuotaService


# from .cuota import CuotaService
partido_schema =PartidoSchema()
partido_repositorio = PartidoRepositorio()

class PartidoService:



    def obtener_partidos_no_finalizados(self):
        # partidos = db.session.query(self.modelo).filter('finalizado' == False).all()
        # return partidos
        pass

    def obtener_partidos(self):
        return partido_repositorio.find_all()

    def obtener_partido_por_id(self, id):
        return partido_repositorio.find_one(id)

    def eliminar_partido(self, id):
        return partido_repositorio.delete(id)

    def actualizar_partido(self, id, data):
        partido = self.obtener_partido_por_id(id)
        for key, value in data.items():
            partido.__setattr__(key, value)
        return partido_repositorio.update(objeto=partido)


    def agregar_partido(self, partido):
            return partido_repositorio.create(partido)


