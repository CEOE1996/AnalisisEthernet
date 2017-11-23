import binascii

def Format(word, char = ':', lenght = 2):
    new_string = ''
    for i in range(0 ,len(word), lenght):
        new_string += word[i:i + lenght] + char
    return new_string[:-1].upper()

def IPFormatFromBin(Datos):
    new_string = ''
    for i in range(0 ,8 * 4, 8):
        new_string += BitToDec(Datos[i:i + 8]) + '.'
    return new_string[:-1].upper()

def IPFormatFromByte(Datos):
    new_string = ''
    for i in range(0 ,1 * 4, 1):
        new_string += ByteToDec(Datos[i:i + 1]) + '.'
    return new_string[:-1].upper()

def IPv6Format(Datos):
    new_string = ''
    for i in range(0 ,8 * 16, 16):
        for j in range(0, 4 * 4, 4):
            new_string += BitToHex(Datos[i + j:i + j + 4])
        new_string +=  ':'
    return new_string[:-1].upper()

def BitToHex(Bit):
    return str(hex(int(Bit, 2)))[2:].upper()

def BitToDec(Bin):
    return str(int(Bin, 2))

def ByteToHex(Bytes):
    return str(binascii.hexlify(Bytes))[2:-1]

def ByteToDec(Byte):
    return str(int.from_bytes(Byte, byteorder='big'))

def HexToByte(Hex):
    return binascii.unhexlify(Hex)#)[2:-1]

def HexToBit(Hex):
    return str(bin(int(Hex, 16))).replace("b", "")

def HexToDec(Hex):
    return str(int(Hex, 16))
