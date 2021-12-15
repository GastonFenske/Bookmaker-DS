from marshmallow import Schema, fields, post_load, post_dump
from main.models import ApuestaModel
from .equipo_schema import EquipoSchema
from .partido_schema import PartidoSchema
from .cliente_schema import ClienteSchema

class ApuestaSchema(Schema):
    id = fields.Int(dump_only=True)
    fecha = fields.DateTime(required=False)
    monto = fields.Float(required=True)
    equipo_ganador_id = fields.Int(required=True, allow_none=True)
    equipo_ganador = fields.Nested(EquipoSchema)
    partido_id = fields.Int(required=True)
    partido = fields.Nested(PartidoSchema)
    cliente_id = fields.Int(required=True)
    ganancia = fields.Float(required=False)
    cliente = fields.Nested(ClienteSchema)

    @post_load
    def make_apuesta(self, data, **kwargs):
        return ApuestaModel(**data)

    SKIP_VALUES = ['equipo_ganador_id', 'partido_id', 'cliente_id']
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items() if key not in self.SKIP_VALUES
        }
