from .. import db


class Repositorio:

    def __init__(self, modelo):
        self.__modelo = modelo

    @property
    def modelo(self):
        return self.__modelo

    def obtener_por_id(self, id):
        objeto = db.session.query(self.modelo).get_or_404(id)
        return objeto

    def obtener_todos(self):
        objetos = db.session.query(self.modelo).all()
        return objetos

    def crear(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto

    def modificar(self, data, id):
        objeto = db.session.query(self.modelo).get_or_404(id)
        for key, value in data:
            setattr(objeto, key, value)
        db.session.add(objeto)
        db.session.commit()
        return objeto

    def eliminar(self, id):
        objeto = db.session.query(self.modelo).get_or_404(id)
        db.session.delete(objeto)
        db.session.commit()

