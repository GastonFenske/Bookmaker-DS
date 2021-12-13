from marshmallow import Schema, fields, validate, post_load
from main.models import CuotaModel

class CuotaSchema(Schema):
    id  = fields.Int(dump_only=True)
    probabilidad_local = fields.Float(required=False)
    probabilidad_empate = fields.Float(required=False)
    probabilidad_visitante = fields.Float(required=False)
    partido_id = fields.Int(required=True)

    @post_load
    def make_cuota(self, data, **kwargs):
        return CuotaModel(**data)