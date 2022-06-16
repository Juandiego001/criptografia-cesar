l = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'Ñ',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z'
]

'''
    Funcion para desencriptar mensaje
'''
def decrypt(m, d):
    d *= -1
    m = m.upper()
    nM = ''
    for i in m:
        if i != ' ':
            v = l.index(i)
            v += d

            if v > 26:
                v -= 27

            nM += l[v]
        else:
            nM += ' '
    
    return nM


'''
    Función para encriptar mensaje
'''
# m: mensaje a encriptar
# d: desplazamiento
# v: valor de acuerdo al arreglo
# nM: nuevo mensaje
def encrypt(m, d):
    m = m.upper()
    nM = ''
    for i in m:
        if i != ' ':
            v = l.index(i)
            v += d

            if v > 26:
                v -= 27

            nM += l[v]
        else:
            nM += ' '
    
    return nM

# Encriptado
me = input('Ingrese el mensaje a encriptar: ')
de = input('Ingrese el desplazamiento: ')
print('Mensaje con cifrado cesar: ' + encrypt(me, int(de)))

# Desencriptado (se toma el mismo desplazamiento)
me = input('\nIngrese el mensaje a desencriptar: ')
# Descomentar la línea de abajo para tomar un desplazamiento diferente
# de = input('Ingrese el desplazamiento: ')
print('Mensaje desencriptado: ' + decrypt(me, int(de)))
        