import Dict
from Dict import *
from Functions import *

def Protocolo(Datos):
    print("Datos:           " + BitToHex(Datos))

def ICMP(Datos):
    print("Tipo Mensaje:    " + Mensaje.get(BitToDec(Datos[:8]), ""))
    print("Codigo Error:    " + Error.get(BitToDec(Datos[8:16]), ""))
    print("Checksum:        " + Datos[16:32])
    print("Datos:           " + BitToHex(Datos[32:]))

def ICMPv6(Datos):
    print("Tipo Mensaje:    " + Dict.TipoMsj.get(BitToDec(Datos[:8]), ""))
    print("Codigo Error:    " + Dict.CodigoMsj[BitToDec(Datos[:8])][int(BitToDec(Datos[8:16]))])
    print("Checksum:        " + BitToHex(Datos[16:32]))
    print("Datos:           " + BitToHex(Datos[32:]))

def TCP(Datos):
    print("Puerto Origen:   " + Dict.Port.get(BitToDec(Datos[:16]), ""))
    print("Puerto Destino:  " + Dict.Port.get(BitToDec(Datos[16:32]), ""))
    print("Num Secuencia:   " + BitToHex(Datos[32:64]))
    print("Acuse Recibo:    " + BitToHex(Datos[64:96]))
    print("Margen de Datos: " + BitToHex(Datos[96:100]))
    print("Reservado:       " + Dict.Reservado.get(Datos[100:106], ""))
    print("Ventana:         " + BitToHex(Datos[106:122]))
    print("Checksum:        " + BitToHex(Datos[122:138]))
    print("Puntero Urgente: " + BitToHex(Datos[138:154]))
    print("Datos:           " + BitToHex(Datos[154:]))

def UDP(Datos):
    print("Puerto Origen:   " + Dict.Port.get(BitToDec(Datos[:16]), ""))
    print("Puerto Destino:  " + Dict.Port.get(BitToDec(Datos[16:32]), ""))
    print("Longitud Total:  " + BitToHex(Datos[32:48]))
    print("Checksum:        " + BitToHex(Datos[48:64]))
    print("DNS")
    print("Identification:  " + BitToDec(Datos[64:80]))
    print("QR:              " + Dict.QR[Datos[80:81]])
    print("OpCode:          " + Dict.OpCodeDNS[BitToDec(Datos[81:85])])
    print("Auth Answer:     " + Dict.AA[Datos[85:86]])
    print("Truncated:       " + Dict.TC[Datos[86:87]])
    print("Recursion Desire:" + Dict.RD[Datos[87:88]])
    print("Recursion Av:    " + Dict.RA[Datos[88:89]])
    print("Z:               " + Datos[89:90])
    print("AD:              " + Datos[90:91])
    print("CD:              " + Datos[91:92])
    print("RCode:           " + Dict.Rcode[BitToDec(Datos[92:96])])
    print("Total Questions: " + BitToDec(Datos[96:112]))
    print("Total Answer:    " + BitToDec(Datos[112:128]))
    print("Total Authority: " + BitToDec(Datos[128:144]))
    print("Total Additional:" + BitToDec(Datos[144:160]))
    print("Datos:           " + BitToHex(Datos[160:]))
