from flask_restful import Resource, request
from main.map import EmpresaSchema
from main.services import EmpresaService

empresa_schema = EmpresaSchema()
empresa_service = EmpresaService()

class Empresa(Resource):

    def get(self):
        return empresa_schema.dump(empresa_service.obtener_empresas(), many=True)

class Empresas(Resource):
    def post(self):
        empresa = empresa_schema.load(request.get_json())
        return empresa_schema.dump(empresa_service.create_empresa(empresa), many=False)

