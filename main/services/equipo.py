from main.repositories.repositorioequipo import EquipoRepositorio

repositorio = EquipoRepositorio()

class EquipoService:
    def obtener_equipos(self):
        return repositorio.find_all()

    def obtener_equipos_de_un_partido(self, objeto):
        return repositorio.find_from_partido(objeto)

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

    def obtener_puntaje_mas_alto(self):
        return repositorio.max_puntaje()

    def verificar_equipo_local(self, objeto):
        return repositorio.verify_equipo_local(objeto)
    
    def verificar_equipo_visitante(self, objeto):
        return repositorio.verify_equipo_visitante(objeto)