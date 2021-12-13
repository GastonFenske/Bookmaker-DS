from main import repositories
from main.repositories import EquipoRepositorio
from main.models import EquipoModel

repositorio = EquipoRepositorio()

class EquipoService:
    def obtener_equipos(self):
        return repositorio.find_all()

    def obtener_equipo_por_id(self, id):
        return repositorio.find_one(id)

    def agregar_equipo(self, objeto):
        return repositorio.create(objeto)

    def eliminar_equipo(self, id):
        return repositorio.delete(id)

    def actualizar_equipo(self, id, data):
        equipo = self.obtener_equipo_por_id(id)
        for key, value in data.items():
            equipo.__setattr__(key, value)
        return repositorio.update(objeto=equipo)