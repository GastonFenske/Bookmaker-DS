from marshmallow import Schema, fields, validate, post_load
from main.models import PartidoModel, EquipoModel
from main.map.couta_schema import CuotaSchema


class PartidoSchema(Schema):
    id = fields.Int(dump_only=True)
    fecha = fields.DateTime(required=True)
    equipo_local_id = fields.Int(required=True)
    equipo_visitante_id = fields.Int(required=True)
    finalizado = fields.Boolean(required=True)
    ganador = fields.Str(required=True)
    goles_local = fields.Int(required=True)
    goles_visitante = fields.Int(required=True)
    partido = fields.Nested(CuotaSchema)

    @post_load
    def make_partido(self, data, **kwargs):
        return PartidoModel(**data)