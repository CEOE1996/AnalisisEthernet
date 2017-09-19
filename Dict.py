import EthType, Prot

Ethertypes = {
                "0800" : EthType.IPv4,
                "0801" : EthType.X75,
                "0802" : EthType.NBS,
                "0803" : EthType.ECMA,
                "0804" : EthType.CHAOSnet,
                "0805" : EthType.X25,
                "0806" : EthType.ARP,
                "0807" : EthType.XNS
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
                    "1"   : Prot.ICMP,
                    "2"   : Prot.Protocolo,
                    "3"   : Prot.Protocolo,
                    "4"   : Prot.Protocolo,
                    "5"   : Prot.Protocolo,
                    "6"   : Prot.Protocolo,
                    "7"   : Prot.Protocolo,
                    "8"   : Prot.Protocolo,
                    "9"   : Prot.Protocolo,
                    "10"  : Prot.Protocolo,
                    "17"  : Prot.Protocolo,
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
            "2" 	:	"el destino no dispone del protocolo solicitado",
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
