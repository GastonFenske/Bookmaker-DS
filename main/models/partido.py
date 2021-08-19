from .. import db

class Partido(db.Model):
    
    __id = db.Column(db.Integer, primary_key=True)
    __fecha = db.Column(db.String(50), nullable=False)
    __equipo_local_id = db.Column(db.Integer, db.ForeignKey('equipo._Equipo__id'), nullable=False)
    equipo_local = db.relationship('Equipo',foreign_keys=[__equipo_local_id])

    __equipo_visitante_id = db.Column(db.Integer, db.ForeignKey('equipo._Equipo__id'), nullable=False)
    equipo_visitante = db.relationship('Equipo', foreign_keys=[__equipo_visitante_id])

    def id_setter(self, id):
        self.__id = id

    def id_getter(self):
        return self.__id

    def fecha_setter(self, fecha):
        self.__fecha = fecha

    def fecha_getter(self):
        return self.__fecha

    def equipo_local_id_setter(self, equipo_local_id):
        self.__equipo_local_id = equipo_local_id

    def equipo_local_id_getter(self):
        return self.__equipo_local_id

    def equipo_visitante_id_setter(self, equipo_visitante_id):
        self.__equipo_visitante_id = equipo_visitante_id

    def equipo_visitante_id_getter(self):
        return self.__equipo_visitante_id

    def to_json(self):
        partido_json = {
            'id': self.__id,
            'fecha': self.__fecha,
            'equipo_local': self.equipo_local.to_json(),
            'equipo_visitante': self.equipo_visitante.to_json()
        }
        return partido_json

    @staticmethod
    def from_json(partido_json):
        partido = Partido()
        partido.id_setter(partido_json.get('id'))
        partido.fecha_setter(partido_json.get('fecha'))
        partido.equipo_local_id_setter(partido_json.get('equipo_local_id'))
        partido.equipo_visitante_id_setter(partido_json.get('equipo_visitante_id'))
        return partido


