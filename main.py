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

me = input('Ingrese el mensaje: ')
de = input('Ingrese el desplazamiento: ')

print('\nMensaje con cifrado cesar: ' + encrypt(me, int(de)))
        