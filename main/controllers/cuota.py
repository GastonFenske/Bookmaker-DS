from flask_restful import Resource
from flask import request
from main.map import CuotaSchema
from main.services import CuotaService
from main.validate import ValidateCuota

cuota_schema = CuotaSchema()
service = CuotaService()
validate_cuota = ValidateCuota()

class Cuotas(Resource):
    def post(self):
        cuota = cuota_schema.load(request.get_json())
        return cuota_schema.dump(service.agregar_cuota(cuota))

    def get(self):
        return cuota_schema.dump(service.obtener_cuotas(), many=True)

class Cuota(Resource):

    def get(self, id):
        @validate_cuota.validar_cuota(id)
        def validated():
            return cuota_schema.dump(service.obtener_cuota(id))
        return validated()




