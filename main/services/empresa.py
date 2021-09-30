from main.repositories import Repositorio
from main.models import EmpresaModel

repositorio = Repositorio(EmpresaModel)

class EmpresaService:
    def obtener_empresas(self):
        return repositorio.obtener_todos()

        