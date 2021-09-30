from .. import db
from sqlalchemy.ext.hybrid import hybrid_property
import datetime as dt

class Apuesta(db.Model):
    __tablename__ = 'apuestas'
    __id = db.Column('id', db.Integer, primary_key=True)
    __fecha = db.Column('fecha', db.DateTime, default=dt.datetime.now(), nullable=False)
    __monto = db.Column('monto', db.Float, nullable=False)
    #__monto_minimo = db.Column('monto_minimo', db.Integer, nullable=False)
    __equipo_ganador_id = db.Column('equipo_ganador', db.ForeignKey('equipos.id'), nullable=False)
    #equipo_ganador = db.relationship('Equipo', back_populates='apuesta')
    __activado = db.Column('activado', db.Boolean, default=True, nullable=False)


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
    def activado(self):
        return self.__activado
    @activado.setter
    def activado(self, activado):
        self.__activado = activado
    @activado.deleter
    def activado(self):
        del self.__activado