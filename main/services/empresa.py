from main.repositories import EmpresaRepositorio

repositorio = EmpresaRepositorio()

class EmpresaService:
    def obtener_empresas(self):
        return repositorio.find_all()

    def obtener_empresa_por_id(self, id):
        return repositorio.find_one(id)

    def create_empresa(self, objeto):
        return repositorio.create(objeto)

        