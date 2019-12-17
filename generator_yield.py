# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 22:14:22 2019

@author: HPC
"""

def generapares(q):
    num = 1
    while num <= q:
        lst = (str(num)+'°' , num *2)
        yield lst
        num += 1

cantidad = int(input('Ingresa canitdad de pares deseados: '))
devpares = generapares(cantidad)

y = ''

# =============================================================================
# El if que hay en el while lo que toma para evaluar la condición es el valor
# que tiene el par y lo divide entre dos para conocer el número de iteración y
# compararla con la cantidad definida, para evitar que se trate de generar un 
# par más allá de lo establecido, ya que eso da un traceback
# =============================================================================
while y != 'N':
    x = next(devpares)
    print()
    print('\t--El' , x[0] , 'par es:' , str(x[1]) )
    y = input('Enter para generar siguiente par ("N" para salir): ')
    if (x[1]/2) >= cantidad:
        break
    
print('\n\t--Se han generado todos los pares solicitados')
