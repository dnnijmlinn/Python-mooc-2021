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

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_funktio_olemassa(self):
        try:
            from src.poista_isot import poista_isot
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä poista_isot(lista: list)')
        try:
            from src.poista_isot import poista_isot
            poista_isot(["Abc"])
        except:
            self.assertTrue(False, 'Varmista että seuraava funktiokutsu onnistuupoista_isot(["Abc"])')

    def test_2_ei_paluuarvo(self):
        poista_isot = load(exercise, function, 'fi')
        val = poista_isot(["Abc"])
        self.assertTrue(type(val) == list, f'Funktio {function} ei palauta listaa kun sitä kutsutaan \npoista_isot(["Abc"])')
    
    def test_3_poistettavat_ei_perakkain(self):
        for test_case in [["EKA", "toka", "KOLMAS", "neljäs"], ["aaaa", "BBBB", "cccc", "dddd", "EEEE", "ffff", "GGGG"]]:
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
