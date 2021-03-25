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

def palabras( letras, largo=0, desde='', hasta='', diccionario=None ):
    lista = []
    for palabra in combLetras(letras,largo):
        if desde and palabra < desde:
            continue
        if hasta and palabra > hasta:
            continue
        if diccionario:
            if not diccionario.check(palabra):
                continue
        lista.append(palabra)
    lista.sort()
    return lista
    
if __name__ == '__main__':
    diccionario = enchant.Dict("en_US")
    print()
    filtrarIngles = ( input('Solo palabras en ingles (S/N)? ') in 'sSyY' )
    desde = input('Filtro Desde (<enter> para no filtrar): ')
    hasta = input('Filtro Hasta (<enter> para no filtrar): ')
    print()
    letras = input('Letras : ')
    while letras:
        largo = int( input('largo : ') )
        print()
        for palabra in palabras( letras, largo, desde, hasta, diccionario if filtrarIngles else None ):
            print(palabra)
        print()
        letras = input('Letras : ')
