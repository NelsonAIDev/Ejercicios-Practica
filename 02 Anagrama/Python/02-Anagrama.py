"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

def comproAnagrama(cadena1 : str, cadena2 : str):

    if cadena1.lower() == cadena2.lower():
        return False
    
    if len(cadena1) != len(cadena2):
        return False
    
    cadena1 = sorted(cadena1.lower())
    cadena2 = sorted(cadena2.lower())

    return cadena1 == cadena2

print(comproAnagrama("abc","cba"))
print(comproAnagrama("abcw","cba"))
print(comproAnagrama("abc","abc"))