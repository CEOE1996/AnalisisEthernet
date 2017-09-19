import Functions, Dict

def IPv4(Datos):
    print("Tipo Ethernet:   DOD Internet Protocol (IPv4)")
    Datos = bin(int(Datos, 16))
    Datos = Datos.replace("b", "")
    print("Version:         " + Datos[:4])
    print("Tamaño:          " + Datos[4:8])
    print("Tipo Servicio:   " + Datos[8:16])
    print("  Prioridad:     " + Dict.Service[Datos[8:11]])
    print("  Retardo:       " + Dict.Retardo[Datos[11]])
    print("  Rendimiento:   " + Dict.Fiabilidad[Datos[12]])
    print("  Fiabilidad:    " + Dict.Fiabilidad[Datos[13]])
    print("Longitud Total:  " + Datos[16:32])
    print("Identificador:   " + Datos[32:48])
    print("Flags:           Reservado, "
                              + Dict.Divisible[Datos[49]] + ', '
                              + Dict.Fragmento[Datos[50]])
    print("Posicion de Frag:" + Datos[51:64])
    print("Tiempo de Vida:  " + Functions.BinToDec(Datos[64:72]))
    Protocolo = Functions.BinToDec(Datos[72:80])
    Dict.FunctProtocolo[Protocolo](Dict.Protocolo[Functions.BinToDec(Protocolo)], Datos[72:])
    
def X75(Datos):
    print("Tipo Ethernet:   X.75 Internet")
    print("Datos:           " + Functions.Format(Datos, ' '))

def NBS(Datos):
    print("Tipo Ethernet:   ECMA Internet")
    print("Datos:           " + Functions.Format(Datos, ' '))

def ECMA(Datos):
    print("Tipo Ethernet:   ECMA Internet")
    print("Datos:           " + Functions.Format(Datos, ' '))

def CHAOSnet(Datos):
    print("Tipo Ethernet:   CHAOSnet")
    print("Datos:           " + Functions.Format(Datos, ' '))

def X25(Datos):
    print("Tipo Ethernet:   X.25 Level 3")
    print("Datos:           " + Functions.Format(Datos, ' '))

def ARP(Datos):
    print("Tipo Ethernet:   Address Resolution Protocol (for IP and CHAOS)")
    print("Datos:           " + Functions.Format(Datos, ' '))

def XNS(Datos):
    print("Tipo Ethernet:   XNS Compatibility")
    print("Datos:           " + Functions.Format(Datos, ' '))
