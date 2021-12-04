from .. import db
from main.models import PartidoModel
from main.repositories import PartidoRepositorio
from main.map import PartidoSchema
from .decorators import validar_equipo


partido_schema =PartidoSchema()
partido_repositorio = PartidoRepositorio()

class PartidoService:
    def obtener_partidos_no_finalizados():
        partidos = db.session.query(PartidoModel).filter('finalizado' == False).all()
        return partidos


    def agregar_partido(self, partido):
        """Agregar partido"""
        @validar_equipo(partido.equipo_local_id)
        @validar_equipo(partido.equipo_visitante_id)
        def guardar_partido():
            """"""
            return partido_schema.dump(partido_repositorio.create(partido))
        return guardar_partido()