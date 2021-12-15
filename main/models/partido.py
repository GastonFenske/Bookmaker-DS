from .. import db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

class Partido(db.Model):
    __tablename__ = 'partidos'
    __id = db.Column('id', db.Integer, primary_key=True)
    __fecha = db.Column('fecha', db.DateTime, default=datetime.now(), nullable=False)
    __equipo_local_id = db.Column('equipo_local', db.Integer, db.ForeignKey('equipos.id'), nullable=False)
    __equipo_visitante_id = db.Column('equipo_visistante', db.Integer, db.ForeignKey('equipos.id'), nullable=False)
    __finalizado = db.Column('finalizado', db.Boolean, default=False)
    __ganador_id = db.Column('ganador', db.Integer, db.ForeignKey('equipos.id'), default=None, nullable=True)
    ganador = db.relationship('Equipo', foreign_keys=[__ganador_id])
    equipo_local = db.relationship('Equipo',foreign_keys=[__equipo_local_id])
    equipo_visitante = db.relationship('Equipo', foreign_keys=[__equipo_visitante_id])
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
    def ganador_id(self):
        return self.__ganador_id
    @ganador_id.setter
    def ganador_id(self, ganador_id):
        self.__ganador_id = ganador_id
    @ganador_id.deleter
    def ganador_id(self):
        del self.__ganador_id
