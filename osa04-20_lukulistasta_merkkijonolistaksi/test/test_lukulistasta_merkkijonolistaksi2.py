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

    def test_3_luvut1(self):
        for test_case in [[0.123, 1.23, 0.0234], [1.222, 0.33333, 0.6666, 0.9999]]:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                muotoile = load(exercise, function, 'fi')
                
                correct = get_correct(test_case)
                test_case2 = test_case[:]
                test_result = muotoile(test_case)

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa odotettua {correct} kutsuttaessa muotoile({test_case2})")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {test_case2} mutta se on {test_case}.")

    def test_4_luvut2(self):
        for test_case in [[1.00023, 0.987, 0.55543, 1.76], [1.0, 2.33333, 44.11]]:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                muotoile = load(exercise, function, 'fi')
                
                correct = get_correct(test_case)
                test_case2 = test_case[:]
                test_result = muotoile(test_case)

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa odotettua {correct} kutsuttaessa muotoile({test_case2})")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {test_case2} mutta se on {test_case}.")
            
if __name__ == '__main__':
    unittest.main()
