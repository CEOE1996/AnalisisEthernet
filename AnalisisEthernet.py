import binascii, IP

def Format(w, c):
    new_string = ''
    for i in range(0 ,len(w), 2):
        new_string += w[i:i+2] + c
    return new_string[:-1].upper()

def X75(Datos):
    print("Tipo Ethernet:   X.75 Internet")
    print("Datos:           " + Format(Datos, ' '))

def NBS(Datos):
    print("Tipo Ethernet:   ECMA Internet")
    print("Datos:           " + Format(Datos, ' '))

def ECMA(Datos):
    print("Tipo Ethernet:   ECMA Internet")
    print("Datos:           " + Format(Datos, ' '))

def CHAOSnet(Datos):
    print("Tipo Ethernet:   CHAOSnet")
    print("Datos:           " + Format(Datos, ' '))

def X25(Datos):
    print("Tipo Ethernet:   X.25 Level 3")
    print("Datos:           " + Format(Datos, ' '))

def ARP(Datos):
    print("Tipo Ethernet:   Address Resolution Protocol (for IP and CHAOS)")
    print("Datos:           " + Format(Datos, ' '))

def XNS(Datos):
    print("Tipo Ethernet:   XNS Compatibility")
    print("Datos:           " + Format(Datos, ' '))

Ethertypes = {
                "0800" : IP.IPv4,
                "0801" : X75,
                "0802" : NBS,
                "0803" : ECMA,
                "0804" : CHAOSnet,
                "0805" : X25,
                "0806" : ARP,
                "0807" : XNS
             }

with open("..\Paquetes Redes\ethernet_ipv4_icmp_redirect.bin", 'rb') as file:
    MacDestino = str(binascii.hexlify(file.read(6)))
    MacOrigen = str(binascii.hexlify(file.read(6)))
    Type = str(binascii.hexlify(file.read(2)))
    Datos = str(binascii.hexlify(file.read(50)))

print("Mac Destino:     " + Format(MacDestino[2:-1], ':'))
print("Mac Origen:      " + Format(MacOrigen[2:-1], ':'))
print("Ethertype:       " + Format(Type[2:-1], ' '))
Ethertypes[Type[2:-1]](Datos[2:-1])
