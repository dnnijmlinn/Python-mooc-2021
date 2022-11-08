import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.summalista'
function = 'summa'

def get_correct(l1: list, l2: list) -> list:
    return [x + y for x,y in zip(l1,l2)]

@points('4.summalista')
class SummalistaTest(unittest.TestCase):
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
            from src.summalista import summa
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä summa(lista1: list, lista2: list)')
        try:
            summa = load(exercise, function, 'fi')
            summa([1],[1])
        except:
            self.assertTrue(False, 'Testaa funktiokutsu\nsumma([1],[1])')


    def test_2_paluuarvon_tyyppi(self):
        summa = load(exercise, function, 'fi')
        val = summa([1],[2])
        self.assertTrue(type(val) == list, f"Funktio {function} ei palauta listaa kutsuttaessa  summa([1],[2])")

    def test_3_lukuja_1(self):
        test_cases = [([1,2,3], [1,2,3]), ([2,4,6], [3,5,7]), ([1,2,1,2,1,2],[2,3,4,5,6,7])]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                summa = load(exercise, function, 'fi')

                correct = get_correct(test_case[0], test_case[1])
                test_case2 = test_case[:]
                test_result = summa(test_case[0], test_case[1])

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa odotettua {correct} kutsuttaessa summa({test_case2})")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {list(test_case2)} mutta se on {list(test_case)}.")

    def test_4_lukuja_2(self):
        test_cases = [([10,10,10,11], [99,999,9,99]), ([-10,-11,-12], [1,2,3]), ([100,101,102,103,104],[99,98,97,96,95])]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                summa = load(exercise, function, 'fi')

                correct = get_correct(test_case[0], test_case[1])
                test_case2 = test_case[:]
                test_result = summa(test_case[0], test_case[1])

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa odotettua {correct} kutsuttaessa summa({test_case2})")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {list(test_case2)} mutta se on {list(test_case)}.")

if __name__ == '__main__':
    unittest.main()
