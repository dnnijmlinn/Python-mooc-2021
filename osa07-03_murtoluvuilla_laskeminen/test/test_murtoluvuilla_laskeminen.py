import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from fractions import Fraction

exercise = 'src.murtoluvuilla_laskeminen'
function = "jaa_palasiksi"

def format(l: list):
    return [str(x) for x in l]



@points('7.murtoluvuilla_laskeminen')
class MurtoluvutTest(unittest.TestCase):
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
            from src.murtoluvuilla_laskeminen import jaa_palasiksi
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä jaa_palasiksi(maara: int)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.murtoluvuilla_laskeminen import jaa_palasiksi
            val = jaa_palasiksi(2)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == list, f"Funktion jaa_merkkeihin pitäisi palauttaa arvo, joka on tyyppiä list, nyt se palauttaa arvon {val} joka on tyyppiä {taip} kun sitä kutsutaan parametrilla 2")
        except:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin parametrin arvolla 2)")

    def test3_import_lause_mukana(self):
        with open("src/murtoluvuilla_laskeminen.py") as f:
            cont = f.read()
            self.assertTrue("import" in cont and "fractions" in cont, 
                f"Ohjelmassasi ei tuoda fractions-kirjastoa käyttöön import-lauseella.")

    def test4_testaa_arvoilla(self):
        f = Fraction
        test_cases = [2, 3, 4, 7, 11, 13, 8]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                jaa_palasiksi = load(exercise, function, 'fi')

                val = jaa_palasiksi(test_case)
                correct = [f(1, test_case)] * test_case

                for i in range(3):
                    self.assertEqual(val, correct, 
                        f"Funktion tulos \n'{val}' \nparametrin arvolla \n'{test_case}' \nei vastaa mallivastausta \n'{correct}'.")

    
    
    
    
              
if __name__ == '__main__':
    unittest.main()
