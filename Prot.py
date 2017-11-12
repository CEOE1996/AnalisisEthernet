import Dict
from Dict import *
from Functions import *

def Protocolo(Datos):
    print("Datos:           " + Datos)

def ICMP(Datos):
    print("Tipo Mensaje:    " + Mensaje.get(BitToDec(Datos[:8]), ""))
    print("Codigo Error:    " + Error.get(BitToDec(Datos[8:16]), ""))
    print("Checksum:        " + Datos[16:32])
    print("Datos:           " + Datos[32:])

def ICMPv6(Datos):
    print("Tipo Mensaje:    " + Dict.TipoMsj.get(BitToDec(Datos[:8]), ""))
    print("Codigo Error:    " + Dict.CodigoMsj[BitToDec(Datos[:8])][int(BitToDec(Datos[8:16]))])
    print("Checksum:        " + Datos[16:32])
    print("Datos:           " + Datos[32:])

def TCP(Datos):
    print("Puerto Origen:   " + Datos[:16])
    print("Puerto Destino:  " + Datos[16:32])
    print("Num Secuencia:   " + Datos[32:64])
    print("Acuse Recibo:    " + Datos[64:96])
    print("Margen de Datos: " + Datos[96:100])
    print("Reservado:       " + Dict.Reservado.get(Datos[100:106], ""))
    print("Ventana:         " + Datos[106:122])
    print("Checksum:        " + Datos[122:138])
    print("Puntero Urgente: " + Datos[138:154])
    print("Datos:           " + Datos[154:])
