
# Hoy jugamos a las funciones recursivas para calcular numeros combinatorios y numeros de Catalan...

import numpy as np  # solo para hacer la comparacion del resoltado de mis funciones contra las de libreria
import scipy as spy # solo para hacer la comparacion del resoltado de mis funciones contra las de libreria

def combin(n, k):
    # Devuelve el numero combinatorio (n k). En realidad esto se puede calcular como n!/(k!(n-k)!) pero hoy me divierto expresandolo 
    # recursivamente como (n-1 k-1) + (n-1 k), igual que lo haríamos manualmente con un triangulo de tartaglia.
    # Obviamente la performance es horrible y apenas probas con numeros un poco mas grandes de 20 o 30 se hace insoportable. 
    # Esto es solo un juego
    if not ( 0 <= k <= n ):
        return 'ERROR, HEREJE!! OJALA QUE SE TE QUEME EL ASADO!!!'
    if n == k:
        return 1
    elif k == 0:
        return 1
    else:
        return combin(n-1, k-1) + combin(n-1, k)

def catalan(n):
    # Devuelve el numero de Catalan C(n). Estos numeros se usan para muchas cosas, 
    # por ejemplo C(n) = cantidad de formas distintas de triangular un poligono de lado n+2
    # C(0) = 1, C(1) = 1, C(n>1) = sum( i=0:n-1 de C(i)*C(n-i-1) )
    # Tambien se puede calcular como (1/n+1)*(2n n) pero hoy me divierto expresandolo en forma recursiva.
    # Obviamente la performance es horrible y apenas probas con numeros un poco mas grandes de 10 o 15 se hace insoportable. 
    # Esto es solo un juego
    if n <= 1:
        return 1
    return sum( [ catalan(i) * catalan(n-1-i) for i in range(n) ] )

def itCombin( n, k ):
    # igual que combin pero resuelto con un metodo iterativo, construyendo el triangulo de tartaglia en 
    # una lista. Tiene mejor resultado incluso que la cuenta con factoriales en cuanto a que muestra los
    # muchas mas cifras significativas en cambio con los factoriales enseguida te lo transforma a float
    if not ( 0 <= k <= n ):
        return 'ERROR, HEREJE!! OJALA QUE SE TE QUEME EL ASADO!!!'
    if n == k:
        return 1
    elif k == 0:
        return 1
    comb = [[1]]     # comb[0][0] = 1
    for ni in range(1,n):   # agrego filas del trianguo hasta la numero n-1
        comb.append( [] )
        comb[ni].append(1)                                        # comb[ni][0] = 1
        for ki in range(1,ni):                                    # agrego los items para 0 < k < ni
            comb[ni].append( comb[ni-1][ki-1] + comb[ni-1][ki] )  # (n k) = (n-1 k-1) + (n-1 k)
        comb[ni].append(1)                                        # comb[ni][ni] = 1
    return comb[n-1][k-1] + comb[n-1][k]

def itCatalan(n):
    # Devuelve el numero de Catalan C(n). Estos numeros se usan para muchas cosas, 
    # por ejemplo C(n) = cantidad de formas distintas de triangular un poligono de lado n+2
    # C(0) = 1, C(1) = 1, C(n>1) = sum( i=0:n-1 de C(i)*C(n-i-1) )
    # Tambien se puede calcular como (1/n+1)*(2n n) pero hoy me divierto calculandolo en forma iterativa

    if n <= 1:
        return 1
    cat = [1,1] # cat[0] = 1 y cat[1] = 1
    for nn in range(2,n+1): # agrego a la lista de numeros de catalan todos los valores hasta el n inclusive
        c = 0
        for i in range(nn):
            c = c + cat[i] * cat[nn-i-1]
        cat.append(c)
    return cat[n]

def factoresPrimos( n ):
    fact = [] # lista de pares (primo, potencia) en los que se descompone n
    primo, pot = 2, 0      # pruebo con las potencias de 2
    while n % primo == 0:
        pot += 1
        n = n // primo
    if pot > 0:
        fact.append((primo,pot))
    primo, pot = 3, 0      # pruebo con las potencias de 3
    while n % primo == 0:
        pot += 1
        n = n // primo
    if pot > 0:
        fact.append((primo,pot))
    # El resto de los primos son de la forma 6p-1 o 6p+1 con p un natural, notese que si un numero x es tal
    #     que x % 6 es 0, 2, 3 o 4, no es primo pues seria multiplo de 2 o de 3
    # Pruebo todos los 'candidatos a primo' desde el 5 en adelante hasta que su cuadrado sea mayor que n
    p = 1
    while 6*p - 1 <= n:
        # print(6*p, ' ', end='')
        primo, pot = 6*p-1, 0      # pruebo con las potencias de 6p-1
        while n % primo == 0:
            pot += 1
            n = n // primo
        if pot > 0:
            fact.append((primo,pot))
        primo, pot = 6*p+1, 0      # pruebo con las potencias de 6p+1
        while n % primo == 0:
            pot += 1
            n = n // primo
        if pot > 0:
            fact.append((primo,pot))
        p += 1
    return fact

losTresCubos = {
    33: (8866128975287528,-8778405442862238,-2736111468807040),
    44: (-80538738812075974, 80435758145817515, 12602123297335631),
    3: (569936821221962380720, -569936821113563493509, -472715493453327032)
}

def chk3c(d, n):
    if n in d:
        n1, n2, n3 = d[n][0], d[n][1], d[n][2]
        print('{0} = {1}^3 + {2}^3 + {3}^3'.format(n,n1,n2,n3))
        print()
        n1 = n1 ** 3
        print( n1 )
        print('+')
        n2 = n2 ** 3
        print( n2 )
        print('+')
        n3 = n3 ** 3
        print( n3 )
        print('=')
        print(n1+n2+n3)

        


if __name__ == '__main__':

    print()
    print()
    for n in range(10):
        for k in range(n+1):
            print(combin(n,k), ' ', end='')
        print()
        
    print()
    print()
    for n in range(10):
        for k in range(n+1):
            print(itCombin(n,k), ' ', end='')
        print()

    print()
    print()
    n = int(input('n: '))
    k = int(input('k: '))
    while n != 0 or k != 0:
        it = itCombin(n,k)
        print('iterativa: ', it)
        if (n < 30):
            print('recursiva: ', combin(n,k))
        print('cuenta   : ', np.math.factorial(n)//(np.math.factorial(k)*np.math.factorial(n-k)))
        n = int(input('n: '))
        k = int(input('k: '))

    print()
    print()
    n = int(input('n: '))
    while n != 0:
        it = itCatalan(n)
        print('iterativa: ', it)
        if n < 15:
            print('recursiva: ', catalan(n))
        print('cuenta   : ', (np.math.factorial(2*n)//(np.math.factorial(n)**2))//(n+1))
        n = int(input('n: '))
        

