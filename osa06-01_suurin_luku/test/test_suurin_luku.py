import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.suurin_luku'
function = 'suurin'

def get_correct() -> dict:
    pass

testdata = ["luvut.txt"]

import os
from shutil import copyfile

@points('6.suurin_luku')
class SuurinLukuTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen lukua ei pyydetty")]):
            for filename in testdata:
                data_file = os.path.join('test', filename)
                copyfile(data_file, filename)            
            cls.module = load_module(exercise, 'fi')

    @classmethod
    def tearDownClass(cls):
        for filename in testdata:
            os.remove(filename)

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_funktio_olemassa(self):
            try:
                from src.suurin_luku import suurin
            except:
                self.assertTrue(False, f"Koodistasi pitäisi löytyä funktio suurin()")

    def test_2_paluuarvon_tyyppi(self):
            suurin = load(exercise, function, 'fi')

            try:
                val = suurin()
            except:
                 self.assertTrue(False, f"Varmista että funktiokutsu onnistuu\nsuurin()")
            taip = str(type(val)).replace("<class '", '').replace("'>","")
            self.assertTrue(type(val) == int, f"Funktion {function} pitäisi palauttaa kokonaisluku, nyt se palauttaa arvon {val} joka on tyyppiä {taip}.")
    
    def test_3_testaa_paluuarvo(self):
            suurin = load(exercise, function, 'fi')

            val = suurin()
            correct = 9988
            
            self.assertEqual(val, correct, f"Funktiosi palauttaa arvon {val}, oikea vastaus on {correct}.")
          
if __name__ == '__main__':
    unittest.main()
