import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, check_source
from functools import reduce
import os

exercise = 'src.merkit_samat'

@points('4.merkit_samat')
class MerkitSamatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["2"] * 10):
           cls.module = load_module(exercise, 'fi')

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_2_funktio_olemassa(self):
        try:
            from src.merkit_samat import samat
        except:
            self.assertTrue(False, f'koodistasi pitäisi löytyä funktio nimeltään samat')

    def test_3_funktiota_voi_kutsua1(self):
        try:
            from src.merkit_samat import samat
            samat("koodari", 1, 10)
        except:
            self.assertTrue(False, f'varmista että funktiota samat pystyy kutsumaan seuraavasti\nsamat("koodari", 1, 10)')
        try:
            from src.merkit_samat import samat
            samat("koodari", 10, 1)
        except:
            self.assertTrue(False, f'varmista että funktiota samat pystyy kutsumaan seuraavasti samat("koodari", 10, 1)')

if __name__ == '__main__':
    unittest.main()