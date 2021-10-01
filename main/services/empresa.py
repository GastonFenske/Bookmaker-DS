from main.repositories import EmpresaRepositorio
from main.models import EmpresaModel

repositorio = EmpresaRepositorio()

class EmpresaService:
    def obtener_empresas(self):
        return repositorio.find_all()

    def obtener_empresa_por_id(self, id):
        return repositorio.find_one(id)

        