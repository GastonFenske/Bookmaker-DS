from .. import db

class Apuesta(db.Model):
    
    __id = db.Column(db.Integer, primary_key=True)
    __monto = db.Column(db.Integer, nullable=False)
    __monto_minimo = db.Column(db.Integer, nullable=False)


    def id_setter(self, id):
        self.__id = id

    def id_getter(self):
        return self.__id

    def monto_setter(self, monto):
        self.__monto = monto

    def monto_getter(self):
        return self.__monto

    def monto_minimo_setter(self, monto_minimo):
        self.__monto_minimo = monto_minimo

    def monto_minimo_getter(self):
        return self.__monto_minimo