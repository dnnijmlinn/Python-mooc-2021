import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.kertomat'
function = 'kertomat'

def get_correct(test_case: int) -> dict:
    k = lambda n: reduce(lambda a,b: a * b, range(1, n + 1))
    return {i: k(i) for i in range (1, test_case + 1)}

def output(d: dict):
    for key in sorted(d.keys()):
        print(str(key) + ": " + str(d[key]))

@points('5.kertomat')
class KertomatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_funktio_olemassa(self):
        try:
            from src.kertomat import kertomat
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä kertomat(n: int)')
        try:
            kertomat = load(exercise, function, 'fi')
            kertomat(1)
        except:
            self.assertTrue(False, 'Tarkista että funktiota voi kutsua seuraavasti\nkertomat(1)')

    def test_2_paluuarvon_tyyppi(self):
        kertomat = load(exercise, function, 'fi')
        val = kertomat(1)
        self.assertTrue(type(val) == dict, f"Funktion {function} tulisi palauttaa arvo, jonka tyyppi on dict.")
    
    def test_3_kertomat(self):
        test_cases = (1,2,4,3,5,6,8,10)
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                kertomat = load(exercise, function, 'fi')

                value = kertomat(test_case)
                correct = get_correct(test_case)

                self.assertEqual(len(correct), len(value), f"Palautetussa sanakirjassa pitäisi olla {len(correct)} alkiota, mutta siinä on {len(value)} alkiota: \n{value}\nkutsutaessa kertomat({test_case})") 
                self.assertEqual(value, correct, f"Tulos \n{value}\nei vastaa mallivastausta \n{correct}\nkutsutaessa kertomat({test_case})") 
              
if __name__ == '__main__':
    unittest.main()
