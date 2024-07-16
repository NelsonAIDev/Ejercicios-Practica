import unittest
from Anagrama import comproAnagrama

class TestAnagrama(unittest.TestCase):

    def test_anagramas(self):
        self.assertTrue(comproAnagrama("amor", "roma"))
        self.assertTrue(comproAnagrama("españa", "señapa"))
        self.assertTrue(comproAnagrama("Listen", "Silent"))
        self.assertTrue(comproAnagrama("Anagram", "Nagaram"))
    
    def test_no_anagramas(self):
        self.assertFalse(comproAnagrama("amor", "amor"))  # No son anagramas según tu definición
        self.assertFalse(comproAnagrama("Hello", "Oleh"))
        self.assertFalse(comproAnagrama("Python", "Java"))
    
    def test_diferente_longitud(self):
        self.assertFalse(comproAnagrama("abc", "abcd"))
        self.assertFalse(comproAnagrama("abcd", "abc"))
    
    def test_cadenas_vacias(self):
        self.assertFalse(comproAnagrama("", ""))
        self.assertFalse(comproAnagrama("a", ""))

if __name__ == '__main__':
    unittest.main()