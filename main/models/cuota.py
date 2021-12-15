from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

class Cuota(db.Model):
    __tablename__ = 'cuotas'
    __id = db.Column('id', db.Integer, primary_key=True)
    __cuota_local = db.Column('local', db.Float, nullable=False)
    __cuota_empate = db.Column('empate', db.Float, nullable=False)
    __cuota_visitante = db.Column('visitante', db.Float, nullable=False)
    __partido_id = db.Column('partido_id', db.Integer, db.ForeignKey('partidos.id'), nullable=False)
    partido = db.relationship('Partido', back_populates='cuota')

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
    def cuota_local(self):
        return self.__cuota_local

    @cuota_local.setter
    def cuota_local(self, cuota):
        self.__cuota_local = cuota

    @cuota_local.deleter
    def cuota_local(self):
        del self.__cuota_local

    @hybrid_property
    def cuota_empate(self):
        return self.__cuota_empate

    @cuota_empate.setter
    def cuota_empate(self, cuota):
        self.__cuota_empate = cuota

    @cuota_empate.deleter
    def cuota_empate(self):
        del self.__cuota_empate

    @hybrid_property
    def cuota_visitante(self):
        return self.__cuota_visitante

    @cuota_visitante.setter
    def cuota_visitante(self, cuota):
        self.__cuota_visitante = cuota

    @cuota_visitante.deleter
    def cuota_visitante(self):
        del self.__cuota_visitante

    @hybrid_property
    def partido_id(self):
        return self.__partido_id
    @partido_id.setter
    def partido_id(self, id):
        self.__partido_id = id
    @partido_id.deleter
    def partido_id(self):
        del self.__partido_id
