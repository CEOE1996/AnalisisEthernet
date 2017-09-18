import IP, EthType

Ethertypes = {
                "0800" : IP.IPv4,
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
