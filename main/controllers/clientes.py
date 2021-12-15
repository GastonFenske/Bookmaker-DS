from .. import db
from flask_restful import Resource
from main.models import ClienteModel
from flask import request
from main.map import ClienteSchema, ClienteFilters

cliente_schema = ClienteSchema()

class Cliente(Resource):
    
    def get(self, id):
        cliente = db.session.query(ClienteModel).get_or_404(id)
        return cliente_schema.dump(cliente), 201


    def delete(self, id):
        cliente = db.session.query(ClienteModel).get_or_404(id)
        try:
            db.session.delete(cliente)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        cliente = db.session.query(ClienteModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(cliente, key, value)
        try:
            db.session.add(cliente)
            db.session.commit()
            return cliente_schema.dump(cliente), 201
        except:
            return '', 404


class Clientes(Resource):
    
    def get(self):
        clientes = db.session.query(ClienteModel)
        cliente_filters = ClienteFilters(clientes)
        for key, value in request.get_json().items():
            clientes = cliente_filters.filter(key, value)
        return cliente_schema.dump(clientes.all(), many=True)

    def post(self):
        cliente = cliente_schema.load(request.get_json())
        db.session.add(cliente)
        db.session.commit()
        return cliente_schema.dump(cliente), 201