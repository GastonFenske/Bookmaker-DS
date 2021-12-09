from .. import db
from main.models import ApuestaModel, EquipoModel, ClienteModel, PartidoModel
from .command import Command, Tarea
from main.map import ApuestaSchema, apuesta_schema
from .decorators import validar_apuesta, validar_equipo, validar_monto, validar_partido, validar_cliente
from main.repositories import ApuestaRepositorio

apuesta_schema = ApuestaSchema()
apuesta_repositorio = ApuestaRepositorio()

class ApuestaService:
    def registrar_apuestas(self, apuesta):
        tarea = Tarea()
        # tarea.agregar(ValidarEquipo(apuesta.equipo_ganador_id))
        tarea.agregar(ValidarEquipo())
        # tarea.agregar(ValidarMontos())

        tarea.agregar(GuardarApuesta())

        orden_a_ejecutar = tarea.execute(apuesta)
        #print(orden_a_ejecutar, "[ORDEN A EJECUTAR]") 
        tarea.execute(apuesta)
        #return tarea.execute(apuesta)
        #return orden_a_ejecutar


    def agregar_apuesta(self, apuesta):
        """Funcion para agregar una apuesta"""
        #@validar_apuesta(apuesta.equipo_ganador_id, apuesta.monto)
        @validar_cliente(apuesta.cliente)
        @validar_partido(apuesta.partido)
        @validar_equipo(apuesta.equipo_ganador_id)
        @validar_monto(apuesta.monto)
        def guardar_apuesta():
            # db.session.add(apuesta)
            # db.session.commit()
            # return apuesta_schema.dump(apuesta)
            return apuesta_schema.dump(apuesta_repositorio.create(apuesta))
        return guardar_apuesta()

class ValidarEquipo(Command):
    def execute(self, param):
        print('Esta entrando a validar equipo')
        print(param, "[PARAMETRO: que deberia ser un id de equipos]")
        equipo = db.session.query(EquipoModel).get(param.equipo_ganador_id)
        print(equipo, "[EQUIPO]")
        if equipo:
            print('Aca no entra')
            return 'Unauthorized', 401 
            #return True
        else:
            print('Aca si')
            #return 'Hola'
            #return False 
            return 'Equipo no encontrado', 404

class ValidarMontos(Command):
    def execute(self, param):
        pass

class GuardarApuesta(Command):
    def execute(self, param):
        print('ESTA ENTRANDO A GUARDAR APUESTA')
        db.session.add(param)
        db.session.commit()
        return apuesta_schema.dump(param)

class EnviarMail(Command):
    def execute(self, param):
        pass