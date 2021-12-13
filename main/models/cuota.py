from .. import db
from sqlalchemy.ext.hybrid import hybrid_property

class Cuota(db.Model):
    __tablename__ = 'cuotas'
    __id = db.Column('id', db.Integer, primary_key=True)
    __probabilidad_local = db.Column('local', db.Float, nullable=False)
    __probabilidad_empate = db.Column('empate', db.Float, nullable=False)
    __probabilidad_visitante = db.Column('visitante', db.Float, nullable=False)
    __partido_id = db.Column('partido_id', db.Integer, db.ForeignKey('partidos.id'), nullable=False)
    partido = db.relationship('Partido', back_populates='cuota')
    #__equipo_id = db.Column('equipo_id', db.Integer, db.ForeignKey('equipos.id'))
    #equipo = db.relationship('Equipo', back_populates='cuota')

    # def __repr__(self) -> str:
    #     return f'({self.probabilidad_empate, self.probabilidad_local, self.probabilidad_visitante})'

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
    def probabilidad_local(self):
        return self.__probabilidad_local

    @probabilidad_local.setter
    def probabilidad_local(self, probabilidad):
        self.__probabilidad_local = probabilidad

    @probabilidad_local.deleter
    def probabilidad_local(self):
        del self.__probabilidad_local

    @hybrid_property
    def probabilidad_empate(self):
        return self.__probabilidad_empate

    @probabilidad_empate.setter
    def probabilidad_empate(self, probabilidad):
        self.__probabilidad_empate = probabilidad

    @probabilidad_empate.deleter
    def probabilidad_empate(self):
        del self.__probabilidad_empate

    @hybrid_property
    def probabilidad_visitante(self):
        return self.__probabilidad_visitante

    @probabilidad_visitante.setter
    def probabilidad_visitante(self, probabilidad):
        self.__probabilidad_visitante = probabilidad

    @probabilidad_visitante.deleter
    def probabilidad_visitante(self):
        del self.__probabilidad_visitante

    @hybrid_property
    def partido_id(self):
        return self.__partido_id
    @partido_id.setter
    def partido_id(self, id):
        self.__partido_id = id
    @partido_id.deleter
    def partido_id(self):
        del self.__partido_id

    #@hybrid_property
    #def equipo_id(self):
    #    return self.__equipo_id
    #@equipo_id.setter
    #def equipo_id(self, id):
    #    self.__equipo_id = id
    #@equipo_id.deleter
    #def equipo_id(self):
    #    del self.__equipo_id