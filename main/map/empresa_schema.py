from marshmallow import Schema, fields, validate, post_load
from main.models import EmpresaModel

class EmpresaSchema(Schema):

    id = fields.Int(dump_only=True)
    razon_social = fields.String(required=True)
    email = fields.String(required=True)
    activado = fields.Boolean(required=False)

    @post_load
    def make_empresa(self, data, **kwargs):
        return EmpresaModel(**data)
