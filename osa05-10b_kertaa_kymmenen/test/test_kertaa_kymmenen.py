import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.kertaa_kymmenen'
function = 'kertaa_kymmenen'

def get_correct(a: int, b: int) -> dict:
    return {x: x * 10 for x in range(a, b + 1)}

@points('5.kertaa_kymmenen')
class Kertaa10Test(unittest.TestCase):
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
            from src.kertaa_kymmenen import kertaa_kymmenen
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä kertaa_kymmenen(alku: int, loppu: int)')
        try:
            kertaa_kymmenen = load(exercise, function, 'fi')
            kertaa_kymmenen(1,2)
        except:
            self.assertTrue(False, 'Tarkista että funktiota voi kutsua seuraavasti\nkertaa_kymmenen(1, 2)')

    def test_2_paluuarvon_tyyppi(self):
        kertaa_kymmenen = load(exercise, function, 'fi')
        val = kertaa_kymmenen(1,2)
        taip = str(type(val)).replace("<class '", '').replace("'>","")
        self.assertTrue(type(val) == dict, f"Funktion {function} tulisi palauttaa arvo, jonka tyyppi on dict, nyt se palauttaa arvon {val} joka on tyyppiä {taip}.")
    
    def test_3_lukusarjat(self):
        test_cases = ((1,3),(0,6),(2,8),(20,23),(100,110))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                kertaa_kymmenen = load(exercise, function, 'fi')

                value = kertaa_kymmenen(test_case[0], test_case[1])
                correct = get_correct(test_case[0], test_case[1])

                self.assertEqual(len(correct), len(value), f"Palautetussa sanakirjassa pitäisi olla {len(correct)} alkiota, mutta siinä on {len(value)} alkiota: \n{value} kun parametrit ovat {test_case}")
                self.assertEqual(value, correct, f"Tulos \n{value}\nei vastaa mallivastausta \n{correct}\nkun parametrit ovat \n{test_case}")
              
if __name__ == '__main__':
    unittest.main()
