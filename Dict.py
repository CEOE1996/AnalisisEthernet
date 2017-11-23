from EthType import *
from Prot import *
import Prot

EthertypesFn = {
                "0800" : IPv4,
                "0801" : EthType,
                "0802" : EthType,
                "0803" : EthType,
                "0804" : EthType,
                "0805" : EthType,
                "0806" : ARP,
                "0807" : EthType,
                "8035" : ARP,
                "86dd" : IPv6
               }

EtTypes = {
            "0800" : "DOD Internet Protocol (IPv4)",
            "0801" : "X.75 Internet",
            "0802" : "ECMA Internet",
            "0803" : "ECMA Internet",
            "0804" : "CHAOSnet",
            "0805" : "X.25 Level 3",
            "0806" : "Address Resolution Protocol (for IP and CHAOS)",
            "0807" : "XNS Compatibility",
            "8035" : "Reverse Address Resolution Protocol (RARP) (Stanford)",
            "86dd" : "IPv6"
          }

Service = {
            "000" : "De rutina",
            "001" : "Prioritario",
            "010" : "Inmediato",
            "011" : "Relámpago",
            "100" : "Invalidación relámpago",
            "101" : "Procesando llamada crítica y de emergencia",
            "110" : "Control de trabajo de Internet",
            "111" : "Control de red"
           }

Retardo = {
            "0" : "Normal",
            "1" : "Bajo"
          }

Fiabilidad = {
                "0" : "Normal",
                "1" : "Bajo"
             }

Divisible = {
                "0" : "Divisible",
                "1" : "No Divisible"
            }

Fragmento = {
                "0" : "Ultimo Fragmento",
                "1" : "Fragmento Intermedio"
            }

Protocolo = {
                "1"   : "ICMP (Internet Control Message Protocol)",
                "2"   : "IGMP (Internet Group Management Protocol)",
                "3"   : "GGP (Gateway-to-Gateway)",
                "4"   : "IP (IP in IP (encapsulation))",
                "5"   : "ST (Stream)",
                "6"   : "TCP (Transmission Control Protocol)",
                "7"   : "CBT (Core Based Trees)",
                "8"   : "EGP (Exterior Gateway Protocol)",
                "9"   : "IGP (Interior Gateway Protocol)",
                "10"  : "BBN-RCC-MON (BBN RCC Monitoring)",
                "17"  : "UDP (User Datagram Protocol)",
                "18"  : "MUX (Multiplexing Protocool)",
                "27"  : "RDP (Reliable Data Protocol)",
                "28"  : "IRTP (Internet Reliable Transaction Protocol)",
                "45"  : "IDRP (Inter-Domain Routing Protocol)",
                "46"  : "RSVP (Reservation Protocol)",
                "47"  : "GRE (Generic Routing Encapsulation)",
                "48"  : "MHRP (Mobile Host Routing Protocol)",
                "50"  : "ESP (Encapsulating Security Payload)",
                "51"  : "AH (Authentication Header)",
                "54"  : "NARP (NBMA Address Resolution Protocol)",
                "55"  : "MOBILE (IP Mobility)",
                "88"  : "EIGRP (Enhanced Interior Gateway Routing Protocol)",
                "89"  : "OSPF (Open Shortest Path First)",
                "94"  : "IPIP (IP-within-IP Encapsulation Protocol)",
                "95"  : "MICP (Mobile Internetworking Control Protocol)",
                "97"  : "ETHERIP (Ethernet-within-IP Encapsulation)",
                "98"  : "ENCAP (Encapsulation Header)",
                "103" : "PIM (Protocol Independent Multicast)",
                "112" : "VRRP (Virtual Router Redundancy Protocol)",
                "113" : "PGM (PGM Reliable Transport Protocol)",
                "115" : "L2TP (Layer Two Tunneling Protocol)",
                "118" : "STP (Schedule Transfer Protocol)",
                "121" : "SMP (Simple Message Protocol)",
                "131" : "PIPE (Private IP Encapsulation within IP)",
                "132" : "SCTP (Stream Control Transmission Protocol)",
                "133" : "FC (Fibre Channel)",
                "137" : "MPLS-in-IP (Multiprotocol Label Switching in IP)",
                "139" : "HIP (Host Identity Protocol)"
            }

FunctProtocolo = {
                    "1"   : ICMP,
                    "2"   : Prot.Protocolo,
                    "3"   : Prot.Protocolo,
                    "4"   : Prot.Protocolo,
                    "5"   : Prot.Protocolo,
                    "6"   : Prot.TCP,
                    "7"   : Prot.Protocolo,
                    "8"   : Prot.Protocolo,
                    "9"   : Prot.Protocolo,
                    "10"  : Prot.Protocolo,
                    "17"  : Prot.UDP,
                    "18"  : Prot.Protocolo,
                    "27"  : Prot.Protocolo,
                    "28"  : Prot.Protocolo,
                    "45"  : Prot.Protocolo,
                    "46"  : Prot.Protocolo,
                    "47"  : Prot.Protocolo,
                    "48"  : Prot.Protocolo,
                    "50"  : Prot.Protocolo,
                    "51"  : Prot.Protocolo,
                    "54"  : Prot.Protocolo,
                    "55"  : Prot.Protocolo,
                    "88"  : Prot.Protocolo,
                    "89"  : Prot.Protocolo,
                    "94"  : Prot.Protocolo,
                    "95"  : Prot.Protocolo,
                    "97"  : Prot.Protocolo,
                    "98"  : Prot.Protocolo,
                    "103" : Prot.Protocolo,
                    "112" : Prot.Protocolo,
                    "113" : Prot.Protocolo,
                    "115" : Prot.Protocolo,
                    "118" : Prot.Protocolo,
                    "121" : Prot.Protocolo,
                    "131" : Prot.Protocolo,
                    "132" : Prot.Protocolo,
                    "133" : Prot.Protocolo,
                    "137" : Prot.Protocolo,
                    "139" : Prot.Protocolo
                 }

Mensaje = {
            "0" 	:	"Echo Replay (Respuesta de eco)",
            "3"	    :	"Destination Unreacheable (destino inaccesible)",
            "4"	    :	"Source Quench (disminución del tráfico desde el origen)",
            "5"	    :	"Redirect (redireccionar - cambio de ruta)",
            "8"	    :	"Echo (solicitud de eco)",
            "11"	:	"Time Exceeded (tiempo excedido para un datagrama)",
            "12"	:	"Parameter Problem (problema de parâmetros)",
            "13"	:	"Timestamp (solicitud de marca de tiempo)",
            "14"	:	"Timestamp Reply (respuesta de marca de tiempo)",
            "15"	:	"Information Request (solicitud de información) - obsoleto-",
            "16"	:	"Information Reply (respuesta de información) - obsoleto-",
            "17"	:	"Addressmask (solicitud de máscara de dirección)",
            "18"	:	"Addressmask Reply (respuesta de máscara de dirección"
          }

Error = {
            "0" 	:	"No se puede llegar  a la red",
            "1" 	:	"no se puede llegar al host o aplicación de destino",
            "2" 	:	"el destino no dispone del Protocolo solicitado",
            "3" 	:	"no se puede llegar al puerto destino o la aplicación destino no está libre",
            "4" 	:	"se necesita aplicar fragmentación, pero el flag correspondiente indica lo contrario",
            "5" 	:	"la ruta de origen no es correcta",
            "6" 	:	"no se conoce la red destino",
            "7" 	:	"no se conoce el host destino",
            "8" 	:	"el host origen está aislado",
            "9" 	:	"la comunicación con la red destino está prohibida por razones administrativas",
            "10" 	:	"la comunicación con el host destino está prohibida por razones administrativas",
            "11" 	:	"no se puede llegar a la red destino debido al Tipo de servicio",
            "12" 	:	"no se puede llegar al host destino debido al Tipo de servicio",

        }

TypeHW = {
            "0" 	:	"Reserved",
            "1"	    :	"Ethernet (10Mb)",
            "2"	    :	"Experimental Ethernet (3Mb)",
            "3"	    :	"Amateur Radio AX.25",
            "4"	    :	"Proteon ProNET Token Ring",
            "5"	    :	"Chaos",
            "6"	    :	"IEEE 802 Networks",
            "7"	    :	"ARCNET",
            "8"	    :	"Hyperchannel",
            "9"	    :	"Lanstar",
            "10"	:	"Autonet Short Address",
            "11"	:	"LocalTalk",
            "12"	:	"LocalNet (IBM PCNet or SYTEK LocalNET)",
            "13"	:	"Ultra link",
            "14"	:	"SMDS",
            "15"	:	"Frame Relay",
            "16"	:	"Asynchronous Transmission Mode (ATM)",
            "17"	:	"HDLC",
            "18"	:	"Fibre Channel",
            "19"	:	"Asynchronous Transmission Mode (ATM)",
            "20"	:	"Serial Line",
            "21"	:	"Asynchronous Transmission Mode (ATM)",
            "22"	:	"MIL-STD-188-220",
            "23"	:	"Metricom",
            "24"	:	"IEEE 1394.1995",
            "25"	:	"MAPOS",
            "26"	:	"Twinaxial",
            "27"	:	"EUI-64",
            "28"	:	"HIPARP",
            "29"	:	"IP and ARP over ISO 7816-3",
            "30"	:	"ARPSec",
            "31"	:	"IPsec tunnel",
            "32"	:	"InfiniBand (TM)",
            "33"	:	"TIA-102 Project 25 Common Air Interface (CAI)",
            "34"	:	"Wiegand Interface",
            "35"	:	"Pure IP",
            "36"	:	"HW_EXP1",
            "37"	:	"HFI",
            "256"	:	"HW_EXP2",
            "257"	:	"AEthernet",
            "65535"	:	"Reserved"
         }

OpCode = {
            "0" 	:	"Reserved",
            "1"	    :	"REQUEST",
            "2"	    :	"REPLY",
            "3"	    :	"request Reverse",
            "4"	    :	"reply Reverse",
            "5"	    :	"DRARP-Request",
            "6"	    :	"DRARP-Reply",
            "7"	    :	"DRARP-Error",
            "8"	    :	"InARP-Request",
            "9"	    :	"InARP-Reply",
            "10"	:	"ARP-NAK",
            "11"	:	"MARS-Request",
            "12"	:	"MARS-Multi",
            "13"	:	"MARS-MServ",
            "14"	:	"MARS-Join",
            "15"	:	"MARS-Leave",
            "16"	:	"MARS-NAK",
            "17"	:	"MARS-Unserv",
            "18"	:	"MARS-SJoin",
            "19"	:	"MARS-SLeave",
            "20"	:	"MARS-Grouplist-Request",
            "21"	:	"MARS-Grouplist-Reply",
            "22"	:	"MARS-Redirect-Map",
            "23"	:	"MAPOS-UNARP",
            "24"	:	"OP_EXP1",
            "25"	:	"OP_EXP2",
            "65535"	:	"Reserved"
         }

TipoMsj = {
            "1"     : "Destino Inaccesible",
            "2"     : "Paquete Demasiado Grande",
            "3"     : "Tiempo Excedido",
            "4"     : "Problema de Parametros"
          }

CodigoMsj = {
                "1"     : (
                            "No existe ruda al destino",
                            "Comunicación con el destino administrativamente prohibida",
                            "No asignado",
                            "Dirección inalcanzable",
                            "Puerto inalcanzable"
                          ),
                "3"     : (
                            "Limite de saltos excedido",
                            "Limite excedido en el reensamble del paquete"
                          ),
                "4"     : (
                            "Error en el campo de encabezado",
                            "Tipo de siguiente encabezado desconocido",
                            "Opción IPv6 desconocida"
                          ),
                "128"   : (
                            "Solicitud de Eco"
                          ),
                "129"   : (
                            "Respuesta de Eco"
                          )
            }

NextHeaderFn = {
                 "58" : ICMPv6
               }

Reservado = {
                "100000" : "URG",
                "010000" : "ACK",
                "001000" : "PSH",
                "000100" : "RST",
                "000010" : "SYN",
                "000001" : "FIN"
            }

QR = {
        "0" : "Query",
        "1" : "Response"
     }

AA = {
        "0" : "Not authoritative",
        "1" : "Is authoritative."
     }

TC = {
        "0" : "Not truncated",
        "1" : "Message truncated"
     }

RD = {
        "0" : "Recursion not desired",
        "1" : "Recursion desired"
     }

RA = {
        "0" : "Recursive query support not available",
        "1" : "Recursive query support available"
     }

Port = {
            "21" 	:	"FTP",
            "22"	:	"SSH",
            "23"	:	"Telnet",
            "25"	:	"SMTP",
            "66"	:	"Oracle SQLNet",
            "79"	:	"Finger",
            "80"	:	"HTTP - Web",
            "107"	:	"Remote Telnet Service",
            "110"	:	"POP3",
            "118"	:	"SQL Services",
            "119"	:	"NNTP - News",
            "137"	:	"NetBios Name Service",
            "138"	:	"NetBios Datagram Service",
            "139"	:	"NetBios Session Service",
            "150"	:	"SQL-Net",
            "161"	:	"Snmp",
            "194"	:	"IRC - Internet Relay Chat",
            "209"	:	"Quick Mail Protocol",
            "217"	:	"dBASE Unix",
            "389"	:	"NetMeeting",
            "407"	:	"Timbuktu pro",
            "443"	:	"HttpS",
            "445"	:	"Microsoft-Ds",
            "515"	:	"printer",
            "522"	:	"NetMeeting",
            "531"	:	"Conference",
            "992"	:	"Telnet SSL",
            "993"	:	"IMAP4 SSL",
            "995"	:	"POP3 SSL",
            "1417"	:	"Timbuktu pro",
            "1418"	:	"Timbuktu pro",
            "1419"	:	"Timbuktu pro",
            "1420"	:	"Timbuktu pro",
            "1547"	:	"LapLink",
            "3000"	:	"Calista IP phone (saliente)",
            "3128"	:	"Squid Proxy",
            "3389"	:	"Microsoft Terminal Server",
            "4099"	:	"AIM Talk",
            "5190"	:	"Calista IP phone (entrante)",
            "5500"	:	"VNC (Virtual Network Computing)",
            "5631"	:	"pcAnyWhere (host)",
            "5632"	:	"pcAnyWhere (host)",
            "5800"	:	"VNC (Virtual Network Computing)",
            "5900"	:	"VNC (Virtual Network Computing)",
            "6346"	:	"SwapNut",
            "6891"	:	"MSN Messenger (archivos)",
            "6892"	:	"MSN Messenger (archivos)",
            "6893"	:	"MSN Messenger (archivos)",
            "6894"	:	"MSN Messenger (archivos)",
            "6895"	:	"MSN Messenger (archivos)",
            "6896"	:	"MSN Messenger (archivos)",
            "6897"	:	"MSN Messenger (archivos)",
            "6898"	:	"MSN Messenger (archivos)",
            "6899"	:	"MSN Messenger (archivos)",
            "6900"	:	"MSN Messenger (archivos)",
            "6901"	:	"MSN Messenger (voz)",
            "20000"	:	"ICQ",
            "20001"	:	"ICQ",
            "20002"	:	"ICQ",
            "20003"	:	"ICQ",
            "20004"	:	"ICQ",
            "20005"	:	"ICQ",
            "20006"	:	"ICQ",
            "20007"	:	"ICQ",
            "20008"	:	"ICQ",
            "20009"	:	"ICQ",
            "20010"	:	"ICQ",
            "20011"	:	"ICQ",
            "20012"	:	"ICQ",
            "20013"	:	"ICQ",
            "20014"	:	"ICQ",
            "20015"	:	"ICQ",
            "20016"	:	"ICQ",
            "20017"	:	"ICQ",
            "20018"	:	"ICQ",
            "20019"	:	"ICQ"
       }

OpCodeDNS = {
                "0"     :   "QUERY, Standard query",
                "1"     :   "IQUERY, Inverse query",
                "2"     :   "STATUS, Server status request",
                "3"     :   "Reserved",
                "4"     :   "Notify",
                "5"     :   "Update",
                "6"     :   "Reserved",
                "7"     :   "Reserved",
                "8"     :   "Reserved",
                "9"     :   "Reserved",
                "10"     :  "Reserved",
                "11"     :  "Reserved",
                "12"     :  "Reserved",
                "13"     :  "Reserved",
                "14"     :  "Reserved",
                "15"     :  "Reserved"
            }

Rcode = {
            "0" 	:	"No error. The request completed successfully",
            "1" 	:	"Format error. The name server was unable to interpret the query",
            "2" 	:	"Server failure. The name server was unable to process this query due to a problem with the name server",
            "3" 	:	"Name Error. Meaningful only for responses from an authoritative name server, this code signifies that the domain name referenced in the query does not exist",
            "4" 	:	"Not Implemented. The name server does not support the requested kind of query",
            "5" 	:	"Refused. The name server refuses to perform the specified operation for policy reasons. For example, a name server may not wish to provide the information to the particular requester, or a name server may not wish to perform a particular operation (e.g., zone transfer) for particular data",
            "6" 	:	"YXDomain. Name Exists when it should not",
            "7" 	:	"YXRRSet. RR Set Exists when it should not",
            "8" 	:	"NXRRSet. RR Set that should exist does not",
            "9" 	:	"NotAuth. Server Not Authoritative for zone",
            "10" 	:	"NotZone. Name not contained in zone",
            "11" 	:	"Reserved",
            "12" 	:	"Reserved",
            "13" 	:	"Reserved",
            "14" 	:	"Reserved",
            "15" 	:	"Reserved"
        }
