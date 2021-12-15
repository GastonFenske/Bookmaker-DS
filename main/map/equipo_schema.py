from marshmallow import Schema, fields, post_load, post_dump
from main.models import EquipoModel

class EquipoSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.String(required=True)
    escudo = fields.String(required=True)
    pais = fields.String(required=True)
    puntaje = fields.Float(required=False, Default=0.0)
    activado = fields.Boolean(required=False)

    @post_load
    def make_equipo(self, data, **kwargs):
        return EquipoModel(**data)


    SKIP_VALUES = ['activado']
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items() if key not in self.SKIP_VALUES
        }