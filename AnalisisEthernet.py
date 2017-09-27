import binascii
from Functions import *
from Dict import *

with open("..\Paquetes Redes\ethernet_arp_request.bin", 'rb') as file:
    MacDestino = ByteToHex(file.read(6))
    MacOrigen = ByteToHex(file.read(6))
    Type = ByteToHex(file.read(2))
    Datos = ByteToHex(file.read(50))

print("Mac Destino:     " + Format(MacDestino, ':'))
print("Mac Origen:      " + Format(MacOrigen, ':'))
print("Ethertype:       " + Format(Type, ' '))
print("Tipo Ethernet:   " + EtTypes[Type])
EthertypesFn[Type](Datos)
