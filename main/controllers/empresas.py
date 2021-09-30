from flask_restful import Resource
from main.map import EmpresaSchema
from main.services import EmpresaService

empresa_schema = EmpresaSchema()
empresa_service = EmpresaService()

class Empresa(Resource):

    def get(self):
        return empresa_schema.dump(empresa_service.obtener_empresas(), many=True)
