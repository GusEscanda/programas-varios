# pip install pyenchant
import enchant

def combLetras( letras, largo = 0 ):
# devuelve todas las combinaciones posibles de palabras de longitud 'largo' que pueden formarse con las letras del string 'letras' 
# (sin repetir letra salvo que ésta aparezca varias veces en 'letras')
    if largo <= 0 or largo > len(letras):
        largo = len(letras)
    
    if largo == 0:
        return []
    elif largo == 1:
        return list(letras)
    else:
        lista = []
        for i in range(len(letras)):
            for p in combLetras( letras[:i]+letras[i+1:], largo-1 ):
                if letras[i] + p not in lista:
                    lista.append( letras[i] + p )
        return lista

def palabrasIngles( dic, letras, largo = 0 ):
    lista = []
    for p in combLetras( letras, largo ):
        if dic.check(p):
            lista.append(p)
    lista.sort()
    for p in lista:
        print(p)

if __name__ == '__main__':
    d = enchant.Dict("en_US")
    letras = input('Letras : ')
    while letras:
        largo = int( input('largo : ') )
        palabrasIngles( d, letras, largo )
        letras = input('Letras : ')
