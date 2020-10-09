# Calular cuanto tiempo falta y cuando terminara un proceso en funcion del total 
# de la tarea y la parte ya relizada

import time

def main():
    total_trabajo = float(input('Total : '))
    comienzo = time.time()
    print('Comienzo : ',time.strftime('%X', time.localtime(comienzo)))
    print()
    trabajo_hecho = float(input('Hecho hasta ahora : '))
    
    while trabajo_hecho < total_trabajo:
        ahora = time.time()
        falta = ( (ahora-comienzo) / trabajo_hecho ) * ( total_trabajo - trabajo_hecho )
        final = ahora + falta
        str_falta = time.strftime( '%X', time.gmtime(falta) )
        str_final = time.strftime( '%X', time.localtime(final) )
        print()
        print( str(int(trabajo_hecho*100/total_trabajo))+'%', '    faltan', str_falta, '    termina', str_final )
        print()
        trabajo_hecho = float(input('Hecho hasta ahora : '))

if __name__ == '__main__':
    main()
