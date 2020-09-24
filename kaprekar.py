

def sortCifras( numero, tipo):
    # Descompone un numero en sus cifras y devuelve el mayor / menor numero que se puede formar con ellas
    # numero: Numero que hay que descomponer en cifras
    # tipo: El tipo de operacion que quiero ('Mayor' / 'Menor')
    # Si el parametro numero es un integer, asume base 10 y devuelve otro integer. Si no, asume una base
    # distinta de 10, lo toma como un string y devuelve otro string.
    decimal = False
    if type(numero) is int:
        numero = str(numero)
        decimal = True
    lista = list( numero )   # transformo numero en la lista de sus cifras
    lista.sort( reverse= (tipo=='Mayor') ) # ordeno la lista
    if decimal:
        n = 0
        for cifra in lista: # convierto la lista ordenada de cifras en un numero entero
            n = n * 10 + int(cifra)
    else:
        n = ''
        for cifra in lista: # convierto la lista ordenada de cifras en un numero expresado como string
            n = n + str(cifra)
    return n

def baseN2int( n, b):
    # convierte un numero (lo recibe como string) en base b a un entero
    # 2 <= b <= 36
    # simbolos : 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
    i = 0
    for cifra in n:
        if cifra in '0123456789':
            i = i * b + int(cifra)
        if cifra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            i = i * b + ( ord(cifra) - ord('A') + 10 )
        if cifra in 'abcdefghijklmnopqrstuvwxyz':
            i = i * b + ( ord(cifra) - ord('a') + 10 )
    return i

def int2BaseN( i, b ):
    # convierte un entero positivo i, a un numero en base b representado en un string
    # 2 <= b <= 36
    # simbolos : 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
    n = '0' if i == 0 else ''
    while i > 0:
        cifra = i % b
        if cifra <= 9:
            n = str(cifra) + n
        else:
            n = chr( ord('A') + cifra - 10 ) + n
        i = i // b
    return n
    

def kaprekar( numero, base = 10):
    # Devuelve la lista de numeros que resulta de someter a 'numero' a un proceso de kaprekar hasta encontrar
    # una repeticion.
    # kaprekar: numero -> mayor numero que se puede formar con sus cifras - menor
    # el numero lo recibe como integer (base 10) o string y base para bases distintas a 10
    # la base puede ser desde 2 hasta 36 (0-9, A-Z)
    if type(numero) is int:
        numero = str(numero)
    listaOperaciones = []
    numeros = []
        
    # solo en caso de la unidad seguida de ceros necesito esto para mantener constante la cantidad de cifras
    cantCifras = len(numero)

    while numero not in numeros:
        if len(numero) < cantCifras: 
            numero = numero + ( '0' * (cantCifras-len(numero)) )
        mayor = sortCifras(numero, tipo='Mayor')
        menor = sortCifras(numero, tipo='Menor')
        dif = baseN2int( mayor, base ) - baseN2int( menor, base )
        dif = int2BaseN( dif, base )
        listaOperaciones.append( ['   ', numero, mayor, menor, dif] )
        numeros.append( numero )
        numero = dif
    listaOperaciones[ numeros.index(numero) ][0] = '***' # marco el repetido para mejorar el informe

    return listaOperaciones


numero = input("Ingresa un numero: ")
while numero:
    base = int( input('Ingrese la base: '))
    for op in kaprekar(numero, base):
        print()
        print('{0} {1}: {2} - {3} = {4}'.format(op[0], op[1], op[2], op[3], op[4]), end='')
    print(' ***')
    print()
    print()
    print()
    numero = input("Ingresa un numero: ")

