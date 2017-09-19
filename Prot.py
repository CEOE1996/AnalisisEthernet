import Functions, Dict

def Protocolo(Name, Datos):
    print("Protocolo:       " + Name)
    print("Checksum:        " + Datos[0:16])
    print("IP Origen:       " + Functions.IPFormatFromBin(Datos[16:48]))
    print("IP Destino:      " + Functions.IPFormatFromBin(Datos[48:80]))
    print("Datos:           " + Datos[80:])

def ICMP(Name, Datos):
    print("Protocolo:       " + Name)
    print("Mensaje:         " + Dict.Mensaje.get(Functions.BinToDec(Datos[0:8]), ""))
    print("Error:           " + Dict.Error.get(Functions.BinToDec(Datos[8:16]), ""))
    print("Checksum:        " + Datos[16:32])
    print("IP Origen:       " + Functions.IPFormatFromBin(Datos[32:64]))
    print("IP Destino:      " + Functions.IPFormatFromBin(Datos[64:96]))
    print("Datos:           " + Datos[96:])
