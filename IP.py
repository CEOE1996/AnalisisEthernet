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

def IPv4(Datos):
    print("Tipo Ethernet:   DOD Internet Protocol (IPv4)")
    Datos = bin(int(Datos, 16))
    Datos = Datos.replace("b", "")
    print("Version:         " + Datos[:4])
    print("Tamaño:          " + Datos[4:8])
    print("Tipo Servicio:   " + Service[Datos[8:11]])
    print("Longitud Total:  " + Datos[16:32])
    print("Identificador:   " + Datos[32:48])
    print("Flags:           " + Datos[48:51])
    print("Posicion de Frag:" + Datos[51:64])
    print("Tiempo de Vida:  " + Datos[64:72])
    print("Protocolo:       " + Datos[72:80])
    print("Checksum:        " + Datos[80:96])
    print("IP Origen:       " + Datos[96:128])
    print("IP Destino:      " + Datos[128:160])
    print("Datos:           " + Datos[160:])
