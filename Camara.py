from Dispositivo import Dispositivo

class Camara (Dispositivo) :

    def __init__(self,id, modelo):
        self.id = id
        self.modelo = modelo
        
    def get_id(self):
        return self.id

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo
    
    def set_id(self, id):
        self.id = id
