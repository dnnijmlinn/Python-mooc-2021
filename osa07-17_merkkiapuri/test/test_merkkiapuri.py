import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.merkkiapuri'
functions = "vaihda_koko puolita poista_erikoismerkit".split()



@points('7.merkkiapuri')
class MerkkiapuriTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)


    def test1_moduli_olemassa(self):
        try:
            import src.merkkiapuri
        except:
            self.assertTrue(False, "Ratkaisustasi pitäisi löytyä määriteltynä moduli nimeltä merkkiapuri.py")

    def test2_funktiot_olemassa(self):
        try:
            from src.merkkiapuri import vaihda_koko, puolita, poista_erikoismerkit
        except:
            self.assertTrue(False, "Modulista merkkiapuri pitäisi löytyä funktiot vaihda_koko, puolita ja poista_erikoismerkit")
    
    def test3_testaa_vaihda_koko(self):
        test_cases = {"aaa": "AAA", "abcdef": "ABCDEF", "testataan": "TESTATAAN", "kaksi eri sanaa": "KAKSI ERI SANAA",
                      "YYY": "yyy", "ABCXYZ": "abcxyz", "TESTISANA": "testisana", "USEAMPI SANA": "useampi sana",
                      "AAAaaa": "aaaAAA", "AaBbCcXxYyZz": "aAbBcCxXyYzZ", "Testi Useammalla SANAlla": "tESTI uSEAMMALLA sanaLLA",
                      "EnTäPä TämÄ": "eNtÄpÄ tÄMä", "MÖRKÖ se lähti PIIRIIN": "mörkö SE LÄHTI piiriin"}

        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                vaihda_koko = load(exercise, functions[0], 'fi')
                try:
                    val = vaihda_koko(test_case)
                    correct = test_cases[test_case]
                    taip = str(type(val)).replace("<class '","").replace("'>","")
                except:
                    self.assertTrue(False, f"Funktion vaihda_koko kutsuminen parametrilla {test_case} aiheutti virheen.")

                self.assertTrue(type(val) == str, f"Funktion vaihda_koko pitäisi palauttaa arvo tyyppiä str kun sitä kutsutaan parametrilla {test_case}, nyt funktio palautti arvon {val}, joka on tyyppiä {taip}")
                self.assertEqual(val, correct, f"Funktio vaihda_koko palauttaa arvon '{val}' parametrin arvolla '{test_case}' kun oikea vastaus olisi ollut {correct}")

    def test4_testaa_puolita(self):
        test_cases = {"abcd": ("ab", "cd"), "ab": ("a", "b"), "111222":("111","222"), "yksikaks": ("yksi","kaks"), 
                      "abcdefg": ("abc", "defg"), "123456789": ("1234", "56789"), "abrakadabra": ("abrak", "adabra")}

        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                puolita = load(exercise, functions[1], 'fi')

                try:
                    val = puolita(test_case)
                    correct = test_cases[test_case]
                    taip = str(type(val)).replace("<class '","").replace("'>","")
                except:
                    self.assertTrue(False, f"Funktion puolita kutsuminen parametrilla {test_case} aiheutti virheen.")

                self.assertTrue(type(val) == tuple, f"Funktion puolita pitäisi palauttaa arvo tyyppiä tuple kun sitä kutsutaan parametrilla {test_case}, nyt funktio palautti arvon {val}, joka on tyyppiä {taip}")
                self.assertTrue(len(val) == 2, f"Funktion puolita pitäisi palauttaa tuplessa kaksi merkkijonoa, nyt palautusarvo on {val}")
                self.assertEqual(val, correct, f"Funktio puolita palauttaa arvon '{val}' parametrin arvolla '{test_case}' kun oikea vastaus olisi ollut {correct}")

    
    def test5_testaa_poista_erikoismerkit(self):
        test_cases = {"moi!": "moi", "Tämäkö testi: testi?": "Tämäkö testi testi", "Voi himputti!!!!111": "Voi himputti111",
                      "a,b.c;d:e_f*g!h#i¤j%k&l/m(n)": "abcdefghijklmn", "(1+3)*2=8": "1328", "Tästä ei poisteta mitään": "Tästä ei poisteta mitään"}

        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                poista_erikoismerkit = load(exercise, functions[2], 'fi')

                try:
                    val = poista_erikoismerkit(test_case)
                    correct = test_cases[test_case]
                    taip = str(type(val)).replace("<class '","").replace("'>","")
                except:
                    self.assertTrue(False, f"Funktion poista_erikoismerkit kutsuminen parametrilla {test_case} aiheutti virheen")

                self.assertTrue(type(val) == str, f"Funktion poista_erikoismerkit pitäisi palauttaa arvo tyyppiä str kun sitä kutsutaan parametrilla {test_case}, nyt funktio palautti arvon {val}, joka on tyyppiä {taip}")
                self.assertEqual(val, correct, f"Funktio poista_erikoismerkit palauttaa arvon '{val}' parametrin arvolla '{test_case}' kun oikea vastaus olisi ollut {correct}")


    
    
    
    
              
if __name__ == '__main__':
    unittest.main()
