import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
import os
import textwrap

exercise = 'src.poista_isot'
function = 'poista_isot'

def get_correct(test_case: list) -> list:
    return [x for x in test_case if not x.isupper()]

@points('4.poista_isot')
class PoistaIsotTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_4_poistettavat_perakkain(self):
        for test_case in [["EKA", "TOKA", "kolmas", "neljäs", "viides"], ["aaaa", "BBBB", "CCCC", "DDDD", "EEEE", "ffff", "GGGG", "HHHH"]]:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                poista_isot = load(exercise, function, 'fi')
                
                correct = get_correct(test_case)
                test_case_original = test_case[:]
                vastaus = poista_isot(test_case)

                self.assertTrue(correct == vastaus, f"Paluuarvo\n{vastaus}\nei vastaa odotettua\n{correct}\nkutsuttaessa poista_isot({test_case_original})")

    def test_5_ei_poistettavia(self):
        for test_case in [["eka", "Toka", "kolmas", "neljäs", "viides"], ["aaaa", "Bbbb", "CCCc", "ddDd", "Eeee", "ffff", "GggG", "hhhh"]]:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                poista_isot = load(exercise, function, 'fi')

                correct = get_correct(test_case)
                test_case_original = test_case[:]
                vastaus = poista_isot(test_case)

                self.assertTrue(correct == vastaus, f"Paluuarvo\n{vastaus}\nei vastaa odotettua\n{correct}\nkutsuttaessa poista_isot({test_case_original})")

if __name__ == '__main__':
    unittest.main()
