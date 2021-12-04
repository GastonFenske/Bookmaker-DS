from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, param):
        pass

class Tarea(Command):
    def __init__(self):
        self.lista = []

    def agregar(self, tarea: Command):
        self.lista.append(tarea)
    
    def execute(self, param):
        for tarea in self.lista:
            print(self.lista, "[LISTA DE TAREAS]")
            print(tarea)
            print(self.lista.index(tarea), "[INDICE DE LA TAREA QUE ESTA RECORRIENDO EL FOR]")
            tarea.execute(param)
            #return tarea.execute(param)