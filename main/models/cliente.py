from .. import db

class Cliente(db.Model):

    __id = db.Column(db.Integer, primary_key=True)
    __nombre = db.Column(db.String(50), nullable=False)
    __apellido = db.Column(db.String(50), nullable=False)
    __email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Cliente: {self.__id} {self.__email}'

    def id_setter(self, id):
        self.__id = id

    def id_getter(self):
        return self.__id

    def nombre_setter(self, nombre):
        self.__nombre = nombre

    def nombre_getter(self):
        return self.__nombre

    def apellido_setter(self, apellido):
        self.__apellido = apellido

    def apellido_getter(self):
        return self.__apellido

    def email_setter(self, email):
        self.__email = email

    def email_getter(self):
        return self.__email

    def to_json(self):
        cliente_json = {
            'id': self.__id,
            'nombre': self.__nombre,
            'apellido': self.__apellido,
            'email': self.__email
        }
        return cliente_json

    @staticmethod
    def from_json(cliente_json):
        cliente = Cliente()
        cliente.id_setter(cliente_json.get('id'))
        cliente.nombre_setter(cliente_json.get('nombre'))
        cliente.apellido_setter(cliente_json.get('apellido'))
        cliente.email_setter(cliente_json.get('email'))
        return cliente

    