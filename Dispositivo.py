from abc import ABC, abstractmethod


class Dispositivo (ABC):
    
    @abstractmethod
    def Transmitir(camara):
        pass