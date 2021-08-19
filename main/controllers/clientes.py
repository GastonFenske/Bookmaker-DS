from .. import db
from flask_restful import Resource
from main.models import ClienteModel
from flask import request, jsonify

class Cliente(Resource):
    
    def get(self, id):

        cliente = db.session.query(ClienteModel).get_or_404(id)
        return cliente.to_json()


    def delete(self, id):
        cliente = db.session.query(ClienteModel).get_or_404(id)
        try:
            db.session.delete(cliente)
            db.session.commit()
            return '', 204
        except:
            return '', 404


class Clientes(Resource):
    
    def get(self):

        clientes = db.session.query(ClienteModel).all()

        return jsonify({
            'clientes': [cliente.to_json() for cliente in clientes]
        })

    def post(self):

        cliente = ClienteModel.from_json(request.get_json())
        db.session.add(cliente)
        db.session.commit()
        return cliente.to_json(), 201