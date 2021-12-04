from .. import db
from main.models import EmpresaModel
from .repositoriobase import Create, Read, Update, Delete
from main.map import EmpresaSchema, empresa_schema

empresa_schema = EmpresaSchema()

class EmpresaRepositorio(Create, Read, Update, Delete):

    # __instancia = None

    # def __new__(cls):
    #     if EmpresaRepositorio.__instancia is None:
    #         print('Nueva instancia')
    #         EmpresaRepositorio.__instancia = object.__new__(cls)
    #         return EmpresaRepositorio.__instancia

    def __init__(self):
        self.__modelo = EmpresaModel

    @property
    def modelo(self):
        return self.__modelo


    def find_all(self):
        objetos = db.session.query(self.modelo).filter(self.modelo.activado == True).all()
        return objetos

    def find_one(self, id):
        objeto = db.session.query(self.modelo).get_or_404(id)
        return objeto

    # def create(self, objeto):
    #     db.session.add(objeto)
    #     db.session.commit()
    #     return objeto

    def create(self, objeto):
        # print("[ENTRA A CREATE DEL REPOSITORIO]")
        instancia = db.session.query(self.modelo).all()
        # print(instancia, "[INSTANCIA]")
        if not instancia:
            # print("[ESTA ENTRANDO A INSTANCIA IS NONE]")
            db.session.add(objeto)
            db.session.commit()
            return empresa_schema.dump(objeto)
        return 'Instancia ya creada', 409

    def delete(self, id):
        objeto = db.session.query(self.modelo).get_or_404(id)
        # db.session.delete(objeto)
        # db.session.commit()
        self.__soft_delete(objeto, id)

    def __soft_delete(self, objeto):
        objeto.__activado = False
        self.update(objeto, id)

    def update(self, data, id):
        objeto = db.session.query(self.modelo).get_or_404(id)
        for key, value in data:
            setattr(objeto, key, value)
        db.session.add(objeto)
        db.session.commit()
        return objeto
