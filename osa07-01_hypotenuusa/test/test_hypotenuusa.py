import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.hypotenuusa'
function = "hypotenuusa"

@points('7.hypotenuusa')
class HypotenuusaTest(unittest.TestCase):
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

    def test1_funktio_olemassa(self):
        try:
            from src.hypotenuusa import hypotenuusa
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä hypotenuusa(k1: float, k2: float)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.hypotenuusa import hypotenuusa
            val = hypotenuusa(1.0,1.0)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == float, f"Funktion hypotenuusa pitäisi palauttaa arvo, joka on tyyppiä float, nyt se palauttaa arvon {val} joka on tyyppiä {taip}")
        except:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin parametrien arvoilla (1.0, 1.0)")

    def test3_import_lause_mukana(self):
        with open("src/hypotenuusa.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "math" in cont, f"Ohjelmassasi ei tuoda math-kirjastosta rutiinia käyttöön import-lauseella.")
    

    def test4_testaa_arvoilla(self):
        test_cases = {(3.0, 4.0): 5.0, (5.0, 12.0): 13.0}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                hypotenuusa = load(exercise, function, 'fi')

                val = hypotenuusa(test_case[0], test_case[1])

                self.assertEqual(val, test_cases[test_case], f"Funktio palautti arvon {val} parametrien arvoilla {test_case}, oikea arvo olisi ollut {test_cases[test_case]}")

    
    
    
    
              
if __name__ == '__main__':
    unittest.main()
