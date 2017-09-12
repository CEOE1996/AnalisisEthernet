import binascii

def Format(word, char = ':', lenght = 2):
    new_string = ''
    for i in range(0 ,len(word), lenght):
        new_string += word[i:i + lenght] + char
    return new_string[:-1].upper()

def IPFormatFromBin(Datos):
    new_string = ''
    for i in range(0 ,8 * 4, 8):
        new_string += BinToDec(Datos[i:i + 8]) + '.'
    return new_string[:-1].upper()

def BinToDec(Bin):
    return str(int(Bin, 2))

def ByteToHex(Bytes):
    return str(binascii.hexlify(Bytes))
