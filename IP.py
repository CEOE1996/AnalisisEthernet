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
    print("Protocolo:       " + Dict.Protocolo[Functions.BinToDec(Datos[72:80])])
    print("Checksum:        " + Datos[80:96])
    print("IP Origen:       " + Functions.IPFormatFromBin(Datos[96:128]))
    print("IP Destino:      " + Functions.IPFormatFromBin(Datos[128:160]))
    print("Datos:           " + Datos[160:])
