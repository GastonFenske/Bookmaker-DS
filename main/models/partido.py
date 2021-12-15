from .. import db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

class Partido(db.Model):
    __tablename__ = 'partidos'
    __id = db.Column('id', db.Integer, primary_key=True)
    __fecha = db.Column('fecha', db.DateTime, default=datetime.now(), nullable=False)
    # __fecha = db.Column('fecha', db.DateTime, default=datetime.now(), nullable=False)
    __equipo_local_id = db.Column('equipo_local', db.Integer, db.ForeignKey('equipos.id'), nullable=False)
    equipo_local = db.relationship('Equipo',foreign_keys=[__equipo_local_id])
    __equipo_visitante_id = db.Column('equipo_visistante', db.Integer, db.ForeignKey('equipos.id'), nullable=False)
    equipo_visitante = db.relationship('Equipo', foreign_keys=[__equipo_visitante_id])
    __finalizado = db.Column('finalizado', db.Boolean, default=False)
    __ganador = db.Column('ganador', db.Integer, default=None, nullable=True)
    # __goles_local = db.Column('goles_local', db.Integer, nullable=False)
    # __goles_visitante = db.Column('goles_visitante', db.Integer, nullable=False)
    cuota = db.relationship('Cuota', back_populates='partido', uselist=False)
    apuestas = db.relationship('Apuesta', back_populates="partido", cascade="all, delete-orphan")


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
    def equipo_local_id(self):
        return self.__equipo_local_id
    @equipo_local_id.setter
    def equipo_local_id(self, id):
        self.__equipo_local_id = id
    @equipo_local_id.deleter
    def equipo_local_id(self):
        del self.__equipo_local_id

    @hybrid_property
    def equipo_visitante_id(self):
        return self.__equipo_visitante_id
    @equipo_visitante_id.setter
    def equipo_visitante_id(self, id):
        self.__equipo_visitante_id = id
    @equipo_visitante_id.deleter
    def equipo_visitante_id(self):
        del self.__equipo_visitante_id

    @hybrid_property
    def finalizado(self):
        return self.__finalizado
    @finalizado.setter
    def finalizado(self, finalizado):
        self.__finalizado = finalizado
    @finalizado.deleter
    def finalizado(self):
        del self.__finalizado

    @hybrid_property
    def ganador(self):
        return self.__ganador
    @ganador.setter
    def ganador(self, ganador):
        self.__ganador = ganador
    @ganador.deleter
    def ganador(self):
        del self.__ganador

    # @hybrid_property
    # def goles_local(self):
    #     return self.__goles_local
    # @goles_local.setter
    # def goles_local(self, goles):
    #     self.__goles_local = goles
    # @goles_local.deleter
    # def goles_local(self):
    #     del self.__goles_local
    
    # @hybrid_property
    # def goles_visitante(self):
    #     return self.__goles_visitante
    # @goles_visitante.setter
    # def goles_visitante(self, goles):
    #     self.__goles_visitante = goles
    # @goles_visitante.deleter
    # def goles_visitante(self):
    #     del self.__goles_visitante

