from Dict import *
from Functions import *

def Protocolo(Datos):
    print("Datos:           " + Datos[80:])

def ICMP(Datos):
    print("Tipo Mensaje:    " + Mensaje.get(BitToDec(Datos[:8]), ""))
    print("Codigo Error:    " + Error.get(BitToDec(Datos[8:16]), ""))
    print("Checksum:        " + Datos[16:32])
    print("Datos:           " + Datos[32:])
