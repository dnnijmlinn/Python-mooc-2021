import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import choice, randint

exercise = 'src.hedelmakauppa'
function = 'lue_hedelmat'

def get_correct() -> dict:
    pass

testdata = ["hedelmat.csv"]

import os
from shutil import copyfile

@points('6.hedelmakauppa')
class HedelmakauppaTest(unittest.TestCase):
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
                from src.hedelmakauppa import lue_hedelmat
            except:
                self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä lue_hedelmat(), varmista että funktion kutsuminen onnistuu!')

    def test_2_paluuarvon_tyyppi(self):
            suurin = load(exercise, function, 'fi')
            try:
                val = suurin()
            except:
                 self.assertTrue(False, f"Varmista että funktiokutsu onnistuu\nlue_hedelmat()")
            taip = str(type(val)).replace("<class '", '').replace("'>","")
            self.assertTrue(type(val) == dict, f"Funktion {function} pitäisi palauttaa sanakirja (eli dict-olio), nyt se palauttaa arvon {val} joka on tyyppiä {taip}.")

    def test_3_testaa_paluuarvo(self):
            suurin = load(exercise, function, 'fi')

            val = suurin()
            correct = {'banaani': 6.5, 'omena': 2.85, 'ananas': 9.5, 'mango': 6.75, 'appelsiini': 5.5, 'viikuna': 11.0, 'mandariini': 5.75, 'pomekranssi': 11.5}
            
            self.assertTrue(val == correct, f"Funktiosi palauttaa arvon\n{val}\noikea vastaus on\n{correct}")
            
if __name__ == '__main__':
    unittest.main()
