import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.muodosta_tuple'
function = 'tee_tuple'

@points('5.muodosta_tuple')
class MuodostaTupleTest(unittest.TestCase):
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
            from src.muodosta_tuple import tee_tuple
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä tee_tuple(x: int, y: int, z: int)' )
        try:
            from src.muodosta_tuple import tee_tuple
            tee_tuple(1,2,3)
        except:
            self.assertTrue(False, 'Tarkista että funktiota voi kutsua seuraavasti\ntee_tuple(1,2,3)' )

    def test_2_paluuarvon_tyyppi(self):
        tee_tuple = load(exercise, function, 'fi')
        val = tee_tuple(1,2,3)
        self.assertTrue(type(val) == tuple, f'Funktio {function} ei palauta tuplea kutsulla tee_tuple(1,2,3)')
    
    def test_3_tuplet(self):
        test_cases = ((1,4,2), (10, 8, 5), (100, 101, 102), (-10, -11, -12), (55, 550, 5500))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                tee_tuple = load(exercise, function, 'fi')
                
                correct = (min(test_case), max(test_case), sum(test_case))
                
                try:
                    test_result = tee_tuple(test_case[0], test_case[1], test_case[2])
                except:
                    self.assertTrue(False, f"Varmista että funktio toimii kun parametrit ovat {test_case}")

                self.assertEqual(correct, test_result, f"Tulos '{test_result}' ei vastaa mallivastausta '{correct}' kun parametrit ovat {test_case}")
                
              
if __name__ == '__main__':
    unittest.main()
