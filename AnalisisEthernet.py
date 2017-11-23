from Functions import *
from Dict import *
from winpcapy import WinPcap, WinPcapUtils, WinPcapDevices

def Sniffer(win_pcap, param, header, data):
    MacDestino = ByteToHex(data[:6])
    MacOrigen = ByteToHex(data[6:12])
    Type = ByteToHex(data[12:14])
    Datos = ByteToHex(data[14:])

    print("Mac Destino:     " + Format(MacDestino, ':'))
    print("Mac Origen:      " + Format(MacOrigen, ':'))
    print("Ethertype:       " + Format(Type, ' '))
    print("Tipo Ethernet:   " + EtTypes[Type])
    EthertypesFn[Type](Datos)
    print("\n")

with open("../Paquetes redes/ethernet_ipv4_udp_dns.bin", 'rb') as file:
    Sniffer("", "", "", file.read())

#WinPcapUtils.capture_on("*Oracle*", Sniffer, 2)
