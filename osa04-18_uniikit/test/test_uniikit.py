import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.uniikit'
function = 'uniikit'

def get_correct(test_case: list) -> list:
    pass

@points('4.uniikit')
class UniikitTest(unittest.TestCase):
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
            from src.uniikit import uniikit
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä uniikit(lista: list)')
        try:
            uniikit = load(exercise, function, 'fi')
            uniikit([1,2])
        except:
            self.assertTrue(False, 'Testaa funktiokutsu\nuniikit([1,2])')

    def test_2_paluuarvon_tyyppi(self):
        uniikit = load(exercise, function, 'fi')
        val = uniikit([1,2])
        self.assertTrue(type(val) == list, f"Funktio {function} ei palauta listaa parametrin arvolla [1,2].")
    
    def test_3_lukuja_1(self):
        test_cases = {(1,2,3,1,2,3): [1,2,3], 
                      (5,6,7,8,8,9,9,5): [5,6,7,8,9],
                      (1,10,1,100,1,1000): [1,10,100,1000]}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                pisimmat = load(exercise, function, 'fi')
                
                correct = test_cases[test_case]
                test_case2 = test_case[:]
                test_result = pisimmat(list(test_case))

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa odotettua {correct} kutsuttaessa uniikit({test_case2})")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {list(test_case2)} mutta se on {list(test_case)}.")

    def test_4_lukuja_2(self):
        test_cases = {(3,2,1,3,2,1,3,2,1): [1,2,3], 
                      (9,8,7,6,9,8,7,6,10,3,3,3,3,1): [1,3,6,7,8,9,10],
                      (-1,-2,-1,-2,-3,-3,-3,0,0): [-3,-2,-1,0]}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                pisimmat = load(exercise, function, 'fi')
                
                correct = test_cases[test_case]
                test_case2 = test_case[:]
                test_result = pisimmat(list(test_case))

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa odotettua {correct} kutsuttaessa uniikit({test_case2})")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {list(test_case2)} mutta se on {list(test_case)}.")
              
if __name__ == '__main__':
    unittest.main()
