import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.lukulistasta_merkkijonolistaksi'
function = 'muotoile'

def get_correct(test_case: list) -> list:
    return [f"{x:.2f}" for x in test_case]


@points('4.lukulistasta_merkkijonolistaksi')
class LuvutMerkkijonoiksiTest(unittest.TestCase):
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
            from src.lukulistasta_merkkijonolistaksi import muotoile
            muotoile([0.23])
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä muotoile(luvut: list)')
        try:
            muotoile = load(exercise, function, 'fi')
            muotoile([0.23])
        except:
            self.assertTrue(False, 'Varmista että seuraava funktiokutsu onnistuu muotoile([0.23])')


    def test_2_paluuarvon_tyyppi(self):
        muotoile = load(exercise, function, 'fi')
        val = muotoile([1.23])
        self.assertTrue(type(val) == list, "Funktio muotoile ei palauta listaa parametrin arvolla [1.23].")
       
if __name__ == '__main__':
    unittest.main()
