import Functions

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

def IPv4(Datos):
    print("Tipo Ethernet:   DOD Internet Protocol (IPv4)")
    Datos = bin(int(Datos, 16))
    Datos = Datos.replace("b", "")
    print("Version:         " + Datos[:4])
    print("Tamaño:          " + Datos[4:8])
    print("Tipo Servicio:   " + Datos[8:16])
    print("  Prioridad:     " + Service[Datos[8:11]])
    print("  Retardo:       " + Retardo[Datos[11]])
    print("  Rendimiento:   " + Fiabilidad[Datos[12]])
    print("  Fiabilidad:    " + Fiabilidad[Datos[13]]
    print("Longitud Total:  " + Datos[16:32])
    print("Identificador:   " + Datos[32:48])
    print("Flags:           Reservado, " + Divisible[Datos[49]] + ', ' + Fragmento[Datos[50]])
    print("Posicion de Frag:" + Datos[51:64])
    print("Tiempo de Vida:  " + Datos[64:72])
    print("Protocolo:       " + Datos[72:80])
    print("Checksum:        " + Datos[80:96])
    print("IP Origen:       " + str(int(Datos[96:104], 2)) + '.'
                              + str(int(Datos[104:112], 2)) + '.'
                              + str(int(Datos[112:120], 2)) + '.'
                              + str(int(Datos[120:128], 2)))
    print("IP Destino:      " + str(int(Datos[128:136], 2)) + '.'
                              + str(int(Datos[136:144], 2)) + '.'
                              + str(int(Datos[144:152], 2)) + '.'
                              + str(int(Datos[152:160], 2)))
    print("Datos:           " + Datos[160:])
