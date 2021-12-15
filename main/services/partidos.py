from main.repositories.repositoriopartido import PartidoRepositorio
from main.map import PartidoSchema


partido_schema =PartidoSchema()
partido_repositorio = PartidoRepositorio()

class PartidoService:

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


