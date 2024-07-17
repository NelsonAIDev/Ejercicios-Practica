"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

def Esprimo(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for i in range(1,100+1):
    if Esprimo(i) == True:
        print(i)
