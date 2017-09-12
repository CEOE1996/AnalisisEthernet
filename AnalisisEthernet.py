import binascii, Functions, Dict

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

with open("..\Paquetes Redes\ethernet_ipv4_icmp_redirect.bin", 'rb') as file:
    MacDestino = str(binascii.hexlify(file.read(6)))
    MacOrigen = str(binascii.hexlify(file.read(6)))
    Type = str(binascii.hexlify(file.read(2)))
    Datos = str(binascii.hexlify(file.read(50)))

print("Mac Destino:     " + Functions.Format(MacDestino[2:-1], ':'))
print("Mac Origen:      " + Functions.Format(MacOrigen[2:-1], ':'))
print("Ethertype:       " + Functions.Format(Type[2:-1], ' '))
Dict.Ethertypes[Type[2:-1]](Datos[2:-1])
