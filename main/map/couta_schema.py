from marshmallow import Schema, fields, validate, post_load, post_dump
from main.models import CuotaModel
from .partido_schema import PartidoSchema

class CuotaSchema(Schema):
    id  = fields.Int(dump_only=True)
    cuota_local = fields.Float(required=False)
    cuota_empate = fields.Float(required=False)
    cuota_visitante = fields.Float(required=False)
    partido_id = fields.Int(required=True)
    partido = fields.Nested(PartidoSchema)

    @post_load
    def make_cuota(self, data, **kwargs):
        return CuotaModel(**data)

    SKIP_VALUES = ['partido_id']
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items() if key not in self.SKIP_VALUES
        }