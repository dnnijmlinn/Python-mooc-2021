import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.vokaalit_pois'
function = 'ilman_vokaaleja'

def get_correct(test_case: str) -> str:
    return "".join([x for x in test_case if x not in "aeiouyåäö"])


@points('4.vokaalit_pois')
class VokaalitPoisTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_4_lauseet(self):
        for test_case in ["tämä on pidempi lause", "testi, jossa on useampi sana", "heipparallaa vaan kaikki!"]:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                ilman_vokaaleja = load(exercise, function, 'fi')
                
                correct = get_correct(test_case)
                test_result = ilman_vokaaleja(test_case)

                self.assertEqual(correct, test_result, f'Palautettu merkkijono\n{test_result}\nei vastaa odotettua\n{correct}\nkutsuttaessa ilman_vokaaleja("{test_case}")')

    def test_5_ei_vokaaleja(self):
        for test_case in ["xzcvb", "grrrrr", "bdfghjklw"]:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                ilman_vokaaleja = load(exercise, function, 'fi')
                
                correct = get_correct(test_case)
                test_result = ilman_vokaaleja(test_case)

                self.assertEqual(correct, test_result, f'Palautettu merkkijono\n{test_result}\nei vastaa odotettua\n{correct}\nkutsuttaessa ilman_vokaaleja("{test_case}")')

    def test_6_vain_vokaaleja(self):
        for test_case in ["aeio","uuuuoooaaaa"]:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                ilman_vokaaleja = load(exercise, function, 'fi')
                
                correct = get_correct(test_case)
                test_result = ilman_vokaaleja(test_case)

                self.assertEqual(correct, test_result, f'Palautettu merkkijono\n{test_result}\nei vastaa odotettua\n{correct}\nkutsuttaessa ilman_vokaaleja("{test_case}")')

if __name__ == '__main__':
    unittest.main()
