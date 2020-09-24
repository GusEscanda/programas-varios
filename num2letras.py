

def num2letrasDigito(n):
    return ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve'][ n % 10 ]

def num2letrasDecenas(n):
    if n < 10:
        return num2letrasDigito(n)

    letras = [ 'diez', 'veinte', 'treinta', 'cuarenta', 
               'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa' ][ n//10 - 1 ]
    if n % 10 == 0:
        return letras

    if n < 20:
        if n < 16:
            letras = ['once', 'doce', 'trece', 'catorce', 'quince'][ n - 11 ]
        else:
            letras = 'dieci' + num2letrasDigito( n % 10 )
    elif n < 30:
        letras = letras[:-1] + 'i' + num2letrasDigito( n % 10 )
    else:
        letras = letras + ' y ' + num2letrasDigito( n % 10 )
    return letras

def num2letrasCentenas( n ):
    if n < 100:
        return num2letrasDecenas(n)

    letras = [ 'cien', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 
               'seiscientos', 'setecientos', 'ochocientos', 'novecientos' ][ n // 100 - 1 ]
    if n % 100 == 0:
        return letras

    if n < 200:
        letras = letras + 'to ' + num2letrasDecenas( n % 100 )
    else:
        letras = letras + ' ' + num2letrasDecenas( n % 100 )
    return letras

def num2letrasMiles(n):
    if n < 1000:
        return num2letrasCentenas(n)
    
    letras = num2letrasCentenas( n // 1000 )
    if ( n // 1000 ) % 10 == 1 and ( n // 1000 ) % 100 != 11: # si los miles terminan en 1 pero no en 11
        letras = letras[:-1]

    letras = letras + ' mil'
    if n % 1000 > 0:
        letras = letras + ' ' + num2letrasCentenas( n % 1000 )

    return letras


def num2letrasMillones(n):
    if n < 10**6:
        return num2letrasMiles(n)
    
    letras = num2letrasMiles( n // 10**6 )
    if ( n // 10**6 ) % 10 == 1 and ( n // 10**6 ) % 100 != 11: # si los millones terminan en 1 pero no en 11
        letras = letras[:-1]

    letras = letras + ( ' millones' if n // 10**6 != 1 else ' millon' )
    if n % 10**6 > 0:
        letras = letras + ' ' + num2letrasMiles( n % 10**6 )

    return letras

def num2letrasBillones(n):
    if n < 10**12:
        return num2letrasMillones(n)
    
    letras = num2letrasMillones( n // 10**12 )
    if ( n // 10**12 ) % 10 == 1 and ( n // 10**12 ) % 100 != 11: # si los billones terminan en 1 pero no en 11
        letras = letras[:-1]

    letras = letras + ( ' billones' if n // 10**12 != 1 else ' billon' )
    if n % 10**12 > 0:
        letras = letras + ' ' + num2letrasMillones( n % 10**12 )

    return letras

def num2letrasTrillones(n):
    if n < 10**18:
        return num2letrasBillones(n)

    letras = num2letrasBillones( n // 10**18 )
    if ( n // 10**18 ) % 10 == 1 and ( n // 10**18 ) % 100 != 11: # si los billones terminan en 1 pero no en 11
        letras = letras[:-1]

    letras = letras + ( ' trillones' if n // 10**18 != 1 else ' trillon' )
    if n % 10**18 > 0:
        letras = letras + ' ' + num2letrasBillones( n % 10**18 )

    return letras

def num2letras(n):
    if n >= 10**24:
        return 'Chiquicientosmil!!!!'
    return num2letrasTrillones(n)

if __name__ == "__main__":
    num = 123
    while num != 0:
        num = int(input('Ingrese numero: '))
        print(num2letras(num))

