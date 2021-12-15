from marshmallow import Schema, fields, post_load, post_dump
from main.models import PartidoModel
from .equipo_schema import EquipoSchema


class PartidoSchema(Schema):
    id = fields.Int(dump_only=True)
    fecha = fields.DateTime(required=False)
    equipo_local_id = fields.Int(required=True)
    equipo_visitante_id = fields.Int(required=True)
    finalizado = fields.Boolean(required=False)
    ganador_id = fields.Int(required=False)
    ganador = fields.Nested(EquipoSchema)
    equipo_local = fields.Nested(EquipoSchema)
    equipo_visitante = fields.Nested(EquipoSchema)

    @post_load
    def make_partido(self, data, **kwargs):
        return PartidoModel(**data)

    SKIP_VALUES = ['equipo_local_id', 'equipo_visitante_id', 'ganador_id']
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items() if key not in self.SKIP_VALUES
        }