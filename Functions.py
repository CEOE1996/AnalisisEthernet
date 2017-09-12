def Format(word, char = ':', lenght = 2):
    new_string = ''
    for i in range(0 ,len(word), lenght):
        new_string += word[i:i + lenght] + char
    return new_string[:-1].upper()
