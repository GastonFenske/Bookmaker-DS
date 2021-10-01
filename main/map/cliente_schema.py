from marshmallow import Schema, fields, validate, post_load
from main.models import ClienteModel

class ClienteSchema(Schema):
    id = fields.Int(dump_only=True)
    apellido = fields.String(required=True)
    nombre = fields.String(required=True)
    email = fields.String(required=True, validate=validate.Email())
    activado = fields.Boolean(required=True)

    @post_load
    def make_cliente(self, data, **kwargs):
        return ClienteModel(**data)