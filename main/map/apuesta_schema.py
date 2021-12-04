from marshmallow import Schema, fields, validate, post_load
from main.models import ApuestaModel

class ApuestaSchema(Schema):
    id = fields.Int(dump_only=True)
    fecha = fields.DateTime(required=False)
    monto = fields.Float(required=True)
    equipo_ganador_id = fields.Int(required=True)
    partido = fields.Int(required=True)
    cliente = fields.Int(required=True)

    @post_load
    def make_apuesta(self, data, **kwargs):
        return ApuestaModel(**data)
