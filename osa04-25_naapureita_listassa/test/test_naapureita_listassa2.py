import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap

exercise = 'src.naapureita_listassa'
function = 'pisin_naapurijono'

def get_correct(test_case: list) -> list:
    pass


@points('4.naapureita_listassa')
class NaapureitaListassaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_4_listat_2(self):
        test_cases = {(1,2,3,0,1,2,3,4,5,3,4,5,1,2,3): 6,
                      (0,1,2,3,4,5,9,10,11,2,3,4): 6,
                      (1,3,5,7,10,11,14,15,19,20,21,22,23,24,25): 7}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                pisin_naapurijono = load(exercise, function, 'fi')
                
                correct = test_cases[test_case]
                test_case2 = test_case[:]
                try:
                    test_result = pisin_naapurijono(list(test_case))
                except:
                    self.assertTrue(False, f"Varmista että metodin suoritus onnistuu parametrilla {test_case2}.")


                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa mallivastausta {correct} testisyötteellä {test_case2}.")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {list(test_case2)} mutta se on {list(test_case)}.")

    def test_5_listat_3(self):
        test_cases = {(1,2,3,5,6,7,6,5,6,7,10,11,10): 7,
                      (0,1,2,1,5,8,7,9,2,3,2): 4,
                      (5,3,4,2,3,1,2,3,9,8,7,8,7,6,7,6): 8}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                pisin_naapurijono = load(exercise, function, 'fi')
                
                correct = test_cases[test_case]
                test_case2 = test_case[:]
                try:
                    test_result = pisin_naapurijono(list(test_case))
                except:
                    self.assertTrue(False, f"Varmista että metodin suoritus onnistuu parametrilla {test_case2}.")


                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa mallivastausta {correct} testisyötteellä {test_case2}.")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {list(test_case2)} mutta se on {list(test_case)}.")
              
if __name__ == '__main__':
    unittest.main()
