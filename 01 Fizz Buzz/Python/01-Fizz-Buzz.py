"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a n "numero ingresado por el usuario "
 * (ambos incluidos, con un salto de línea entre
 * cada impresión si no ingresa un numero n se realizara hasta el 100), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz(n = 100):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0 :
            print("fizzbuzz")
        elif i % 3 == 0 :
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
    exit

fizzbuzz()