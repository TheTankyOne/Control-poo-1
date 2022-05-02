from Dispositivo import Dispositivo
from Camara import Camara

camara_digital = Camara(1,"Camara de Grabacion Digital")
camara_reflex = Camara(2,"Camara Reflex")
camara_videoconferencia = Camara(3,"Camara de Videoconferecia")
camara_webcam = Camara(4,"Webcam")
camara_mobil = Camara(5,"Camara de Dispositivo Mobil")

def Transmitir(camara):
        number = int
        print("1 camara digital, 2 camara reflex, 3 camara videoconferencia, 4 webcam, 5 camara dispositivo movil")
        input(number)

if __name__ == "__main__" :
    print("elija la camara con la que quiera transmitir: \n")
