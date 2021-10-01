from .. import db
from main.models import ApuestaModel
from .command import Command, Tarea

class ApuestaService:
    def registrar_apuestas(self, apuesta):
        tarea = Tarea()
        tarea.agregar(ValidarPartido())
        tarea.agregar(ValidarMontos())
        tarea.agregar(GuardarApuesta())
        tarea.agregar(EnviarMail())
        return tarea.execute(apuesta)

class ValidarPartido(Command):
    def execute(self, param):
        pass

class ValidarMontos(Command):
    def execute(self, param):
        pass

class GuardarApuesta(Command):
    def execute(self, param):
        pass

class EnviarMail(Command):
    def execute(self, param):
        pass