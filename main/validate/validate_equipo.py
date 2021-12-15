from main.services.equipo import EquipoService

service = EquipoService()

class ValidateEquipo():

    def validar_equipos(self, *ids):
        """Decorador para validar mas de un equipo"""
        def decorator(function):
            def wrapper(*args, **kwargs):
                for id in ids:
                    equipo = service.obtener_equipo_por_id(id)
                    if not equipo:
                        return f'El equipo con el id: {id} no ha sido encontrado', 404
                        break
                return function(*args, **kwargs)
            return wrapper
        return decorator
    
    def validar_equipo(self, objeto):
        def decorator(function):
            def wrapper(*args, **kwargs):
                equipos = service.obtener_equipos_de_un_partido(objeto)
                equipos = [e.id for e in equipos]
                if objeto.equipo_ganador_id in equipos or objeto.equipo_ganador_id == None:
                    return function(*args, **kwargs)
                return 'Equipo no encontrado en este partido', 404
            return wrapper
        return decorator

    #quizas aca tambien se puede colocar un strategy
    def validar_equipo_local(self, objeto):
        # partido_local = db.session.query(self.modelo).filter((self.modelo.equipo_local_id == objeto.equipo_ganador_id) & (self.modelo.id == objeto.partido)).count()
        # return True if partido_local != 0 else False
        return service.verificar_equipo_local(objeto)

    def validar_equipo_visitante(self, objeto):
        # partido_visitante = db.session.query(self.modelo).filter((self.modelo.equipo_visitante_id == objeto.equipo_ganador_id) & (self.modelo.id == objeto.partido)).count()
        # return True if partido_visitante != 0 else False
        return service.verificar_equipo_visitante(objeto)

    def validar_equipo_empate(self, objeto):
        """"""
        pass
        # partido_empate = db.session.query(PartidoModel).filter(PartidoModel.equipo_local_id == objeto.partido )
            