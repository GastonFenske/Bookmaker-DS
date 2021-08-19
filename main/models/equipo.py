from .. import db

class Equipo(db.Model):
    
    __id = db.Column(db.Integer, primary_key=True)
    __nombre = db.Column(db.String(50), nullable=False)
    __escudo = db.Column(db.String(120), nullable=False)
    __pais = db.Column(db.String(120), nullable=False)

    def id_setter(self, id):
        self.__id = id

    def id_getter(self):
        return self.__id

    def nombre_setter(self, nombre):
        self.__nombre = nombre

    def nombre_getter(self):
        return self.__nombre

    def escudo_setter(self, escudo):
        self.__escudo = escudo

    def escudo_getter(self):
        return self.__escudo

    def pais_setter(self, pais):
        self.__pais = pais

    def pais_getter(self):
        return self.__pais

    def to_json(self):
        equipo_json = {
            'id': self.__id,
            'nombre': self.__nombre,
            'escudo': self.__escudo,
            'pais': self.__pais
        }
        return equipo_json

    @staticmethod
    def from_json(equipo_json):
        equipo = Equipo()
        equipo.id_setter(equipo_json.get('id'))
        equipo.nombre_setter(equipo_json.get('nombre'))
        equipo.escudo_setter(equipo_json.get('escudo'))
        equipo.pais_setter(equipo_json.get('pais'))
        return equipo