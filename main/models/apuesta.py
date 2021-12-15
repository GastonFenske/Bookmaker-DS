from .. import db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

class Apuesta(db.Model):
    __tablename__ = 'apuestas'
    __id = db.Column('id', db.Integer, primary_key=True)
    __fecha = db.Column('fecha', db.DateTime, default=datetime.now(), nullable=False)
    __monto = db.Column('monto', db.Float, nullable=False)
    __equipo_ganador_id = db.Column('equipo_ganador_id', db.ForeignKey('equipos.id'), nullable=True)
    __partido_id = db.Column('partido', db.Integer, db.ForeignKey('partidos.id'), nullable=False)
    __cliente_id = db.Column('cliente', db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    __ganancia = db.Column('ganacia', db.Float, nullable=False)
    partido = db.relationship('Partido', back_populates='apuestas')
    cliente = db.relationship('Cliente', back_populates='apuestas')
    equipo_ganador = db.relationship('Equipo', back_populates='apuestas')


    @hybrid_property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @id.deleter
    def id(self):
        del self.__id

    @hybrid_property
    def fecha(self):
        return self.__fecha
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha
    @fecha.deleter
    def fecha(self):
        del self.__fecha  



    @hybrid_property
    def monto(self):
        return self.__monto

    @monto.setter
    def monto(self, monto):
        self.__monto = monto
    
    @monto.deleter
    def monto(self):
        del self.__monto

    @hybrid_property
    def monto_minimo(self):
        return self.__monto_minimo

    @monto_minimo.setter
    def monto_minimo(self, monto):
        self.__monto_minimo = monto
    
    @monto_minimo.deleter
    def monto_minimo(self):
        del self.__monto_minimo
    
    @hybrid_property
    def equipo_ganador_id(self):
        return self.__equipo_ganador_id
    @equipo_ganador_id.setter
    def equipo_ganador_id(self, id):
        self.__equipo_ganador_id = id
    @equipo_ganador_id.deleter
    def equipo_ganador_id(self):
        del self.__equipo_ganador_id   

    @hybrid_property
    def partido_id(self):
        return self.__partido_id

    @partido_id.setter
    def partido_id(self, partido_id):
        self.__partido_id = partido_id

    @partido_id.deleter
    def partido_id(self):
        del self.__partido_id

    @hybrid_property
    def cliente_id(self):
        return self.__cliente_id

    @cliente_id.setter
    def cliente_id(self, cliente_id):
        self.__cliente_id = cliente_id

    @cliente_id.deleter
    def cliente_id(self):
        del self.__cliente_id 

    @hybrid_property
    def ganancia(self):
        return self.__ganancia

    @ganancia.setter
    def ganancia(self, ganancia):
        self.__ganancia = ganancia

    @ganancia.deleter
    def ganancia(self):
        del self.__ganancia 

