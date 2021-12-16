from main.services.equipo import EquipoService

service = EquipoService()

class ValidateEquipo():

    def validar_equipos(self, *ids):
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

    def validar_equipo_local(self, objeto):
        return service.verificar_equipo_local(objeto)

    def validar_equipo_visitante(self, objeto):
        return service.verificar_equipo_visitante(objeto)

    def validar_equipo_empate(self, objeto):
        pass
        
            