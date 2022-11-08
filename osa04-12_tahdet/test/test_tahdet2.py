import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.tahdet'
function = 'lista_tahtina'

def get_correct(lst: list) -> str:
    return "\n".join(["*" * x for x in lst])

@points('4.lista_tahtina')
class TahdetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_4_luvut_1(self):
        test_cases = ([2,2],[1,1,1,1],[1,2,3,2,1],[5,4,3,2,1],[2,2,2],[8,6,2,4,6])
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                from src.tahdet import lista_tahtina
                lista_tahtina(test_case)
                
                correct = get_correct(test_case)

                output_alussa = get_stdout()
                lista_tahtina(test_case)
                output = get_stdout().replace(output_alussa+'\n', '', 1)

                self.assertEqual(len(correct), len(output), f"Tulostettujen rivien määrä on väätä testisyötteellä {test_case}. Funktiosi tulosti {len(output)} riviä, oikea määrä on  {len(correct)}")
                self.assertEqual(correct, output, f"Tulos: \n{output}\nei vastaa mallivastausta \n{correct}\ntestisyötteellä {test_case}.")

    def test_5_luvut_2(self):
        test_cases = ([9,9,9,9],[1,0,1,0,1],[5,5,3,3,1,1,3,3,5,5])
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                from src.tahdet import lista_tahtina
                lista_tahtina(test_case)

                correct = get_correct(test_case)

                output_alussa = get_stdout()
                lista_tahtina(test_case)
                output = get_stdout().replace(output_alussa+'\n', '', 1)

                self.assertEqual(correct, output, f"Tulos:\n{output}\nei vastaa mallivastausta \n{correct}\ntestisyötteellä {test_case}.")
        
if __name__ == '__main__':
    unittest.main()
