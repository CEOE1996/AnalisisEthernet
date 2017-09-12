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
            "001": "Prioritario",
            "010": "Inmediato",
            "011": "Relámpago",
            "100": "Invalidación relámpago",
            "101": "Procesando llamada crítica y de emergencia",
            "110": "Control de trabajo de Internet",
            "111": "Control de red"
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
