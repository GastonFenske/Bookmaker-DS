from main.repositories import ClienteRepositorio


repositorio = ClienteRepositorio()
class ClienteService():
    
    def obtener_cliente(self, id):
        return repositorio.find_one(id)