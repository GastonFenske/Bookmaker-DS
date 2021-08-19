from .. import db

class Empresa(db.Model):
    
    __id = db.Column(db.Integer, primary_key=True)
    __razon_social = db.Column(db.String(50), nullable=False)
    __email = db.Column(db.String(120), nullable=False)

    def id_setter(self, id):
        self.__id = id

    def id_getter(self):
        return self.__id

    def razon_social_setter(self, razon):
        self.__razon_social = razon

    def razon_social_getter(self):
        return self.__razon_social

    def email_setter(self, email):
        self.__email = email

    def email_getter(self):
        return self.__email

    