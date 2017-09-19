import binascii, Functions, Dict

with open("..\Paquetes Redes\ethernet_ipv4_icmp.bin", 'rb') as file:
    MacDestino = Functions.ByteToHex(file.read(6))
    MacOrigen = Functions.ByteToHex(file.read(6))
    Type = Functions.ByteToHex(file.read(2))
    Datos = Functions.ByteToHex(file.read(50))

print("Mac Destino:     " + Functions.Format(MacDestino[2:-1], ':'))
print("Mac Origen:      " + Functions.Format(MacOrigen[2:-1], ':'))
print("Ethertype:       " + Functions.Format(Type[2:-1], ' '))
Dict.Ethertypes[Type[2:-1]](Datos[2:-1])
