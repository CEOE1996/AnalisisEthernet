import Dict
import Functions
from Dict import *
from Functions import *

def IPv4(Datos):
    Datos = HexToBit(Datos)
    print("Version:         " + BitToHex(Datos[:4]))
    print("Tamaño:          " + BitToHex(Datos[4:8]))
    print("Tipo Servicio:   ")
    print("  Prioridad:     " + Dict.Service[Datos[8:11]])
    print("  Retardo:       " + Dict.Retardo[Datos[11]])
    print("  Rendimiento:   " + Dict.Fiabilidad[Datos[12]])
    print("  Fiabilidad:    " + Dict.Fiabilidad[Datos[13]])
    print("Longitud Total:  " + BitToHex(Datos[16:32]))
    print("Identificador:   " + BitToHex(Datos[32:48]))
    print("Flags:           Reservado, "
                              + Dict.Divisible[Datos[49]] + ', '
                              + Dict.Fragmento[Datos[50]])
    print("Posicion de Frag:" + BitToHex(Datos[51:64]))
    print("Tiempo de Vida:  " + BitToDec(Datos[64:72]))
    Protocolo = BitToDec(Datos[72:80])
    print("Protocolo:       " + Protocolo)
    print("Protocolo:       " + Dict.Protocolo[Protocolo])
    print("Checksum:        " + BitToHex(Datos[80:96]))
    print("IP Origen:       " + IPFormatFromBin(Datos[96:128]))
    print("IP Destino:      " + IPFormatFromBin(Datos[128:160]))
    Dict.FunctProtocolo[Protocolo](Datos[160:])

def ARP(Datos):
    Datos = HexToByte(Datos)
    print("Tipo Hardware:   " + Dict.TypeHW.get(ByteToDec(Datos[:2]), "Unassigned"))
    print("Tipo Protocolo:  " + Dict.EtTypes[ByteToHex(Datos[2:4])])
    DirecHard = int(ByteToDec(Datos[4:5]))
    DirecProt = int(ByteToDec(Datos[5:6]))
    print("Direc Hardware:  " + str(DirecHard))
    print("Direc Protocolo: " + str(DirecProt))
    print("Cod Operacion:   " + Dict.OpCode.get(ByteToDec(Datos[6:8])), "Unassigned")
    L = 8
    print("Hardware Emisor: " + Format(ByteToHex(Datos[L:L + DirecHard]), ' '))
    L += DirecHard
    print("IP Emisor:       " + IPFormatFromByte(Datos[L:L + DirecProt]))
    L += DirecProt
    print("Hardware Recept: " + Format(ByteToHex(Datos[L:L + DirecHard]), ' '))
    L += DirecHard
    print("IP Recept:       " + IPFormatFromByte(Datos[L:L + DirecProt]))
    L += DirecProt
    print("Datos:           " + Format(ByteToHex(Datos[L:]), ' '))

def EthType(Datos):
    print("Datos:           " + Format(Datos, ' '))

def IPv6(Datos):
    Datos = HexToBit(Datos)
    print("Version:         " + BitToDec(Datos[:4]))
    print("Clase Trafico:   " + BitToDec(Datos[4:12]))
    print("Etiqueta Flujo:  " + BitToDec(Datos[12:32]))
    print("Tamaño Carga:    " + BitToDec(Datos[32:48]))
    print("Encabezado Sig:  " + BitToDec(Datos[48:56]))
    print("Limite Salto:    " + BitToDec(Datos[56:64]))
    print("IP Origen:       " + IPv6Format(Datos[64:192]))
    print("IP Destino:      " + IPv6Format(Datos[192:320]))
    Dict.NextHeaderFn[BitToDec(Datos[48:56])](Datos[320:])
