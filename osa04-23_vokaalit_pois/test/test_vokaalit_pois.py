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

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_funktio_olemassa(self):
        try:
            from src.vokaalit_pois import ilman_vokaaleja
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä ilman_vokaaleja(lause: str)')
        try:
            ilman_vokaaleja = load(exercise, function, 'fi')
            ilman_vokaaleja("abc")
        except:
            self.assertTrue(False, 'Varmista että seuraava funktiokutsu onnistuu ilman_vokaaleja("abc")')

    def test_2_paluuarvon_tyyppi(self):
        ilman_vokaaleja = load(exercise, function, 'fi')
        val = ilman_vokaaleja("abc")
        self.assertTrue(type(val) == str, 'Funktio ilman_vokaaleja ei palauta merkkijonoa kutsuttaessa ilman_vokaaleja("abc").')
    
    def test_3_yksi_sana(self):
        for test_case in ["testisana", "töttöröö", "abrakadabra", "ananasakäämä", "abcdefghijklmnopqrstuvwxyzåäö"]:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                ilman_vokaaleja = load(exercise, function, 'fi')
                
                correct = get_correct(test_case)
                test_result = ilman_vokaaleja(test_case)

                self.assertEqual(correct, test_result, f'Palautettu merkkijono\n{test_result}\nei vastaa odotettua\n{correct}\nkutsuttaessa ilman_vokaaleja("{test_case}")')
if __name__ == '__main__':
    unittest.main()
