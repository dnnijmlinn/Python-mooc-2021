import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.parametrien_validointi'
function = 'uusi_henkilo'

@points('6.parametrien_validointi')
class ParametrienValidointiTest(unittest.TestCase):
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

    def test_1_funktio_olemassa(self):
        try:
            from src.parametrien_validointi import uusi_henkilo
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä uusi_henkilo(nimi: str, ika: int)')

    def test_2_validit_arvot(self):
        test_cases = [("Arto Artonen", 32), ("Matti Mattila",11), ("Maija Maijanen", 33), ("Sirkka-Liisa Virtanen", 97), ("Matti Huuuhaa Innola", 145)]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                uusi_henkilo = load(exercise, function, 'fi')
                try:
                    hlo = uusi_henkilo(test_case[0], test_case[1])
                except ValueError:
                    self.assertTrue(False, f"Funktio antoi virheen syötteellä {test_case}, vaikka parametrit ovat sääntöjen mukaiset!")
                except:
                    self.assertTrue(False, f"Funktion suoritus epäonnistui syötteellä {test_case} - tarkista ohjelmakoodi!")
                self.assertEqual(hlo, test_case, f"Funktion tulisi palauttaa arvo {test_case} kun syöte on {test_case} - nyt funktiosi palautti arvon {hlo}")

    def test_3_huonot_nimet(self):
        test_cases = [("Arto", 32), ("",11), ("Maija", 33), ("Sirkka-Liisa Virtanen-Aftenbladet-Tötterström-Lahtiska-Vanamo-Kullervoinen", 97)]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                uusi_henkilo = load(exercise, function, 'fi')
                try:
                    hlo = uusi_henkilo(test_case[0], test_case[1])
                    self.assertTrue(False, f"Funktio ei antanut virhettä syötteellä {test_case}, vaikka parametrit ovat sääntöjen vastaiset!")
                except ValueError:
                    pass

    def test_4_huonot_iat(self):
        test_cases = [("Arto Artonen", 232), ("Matti Mattila",-11), ("Maija Maijanen", 153)]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                uusi_henkilo = load(exercise, function, 'fi')
                try:
                    hlo = uusi_henkilo(test_case[0], test_case[1])
                    self.assertTrue(False, f"Funktio ei antanut virhettä syötteellä {test_case}, vaikka parametrit ovat sääntöjen vastaiset!")
                except ValueError:
                    pass

                
    
    
    
    
              
if __name__ == '__main__':
    unittest.main()
