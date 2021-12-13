from marshmallow import Schema, fields, validate, post_load, post_dump
from main.models import ApuestaModel
from .equipo_schema import EquipoSchema

class ApuestaSchema(Schema):
    id = fields.Int(dump_only=True)
    fecha = fields.DateTime(required=False)
    monto = fields.Float(required=True)
    equipo_ganador_id = fields.Int(required=True, allow_none=True)
    equipo_ganador = fields.Nested(EquipoSchema)
    partido = fields.Int(required=True)
    cliente = fields.Int(required=True)
    ganancia = fields.Float(required=False)

    @post_load
    def make_apuesta(self, data, **kwargs):
        return ApuestaModel(**data)

    SKIP_VALUES = ['equipo_ganador_id']
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items() if key not in self.SKIP_VALUES
        }
