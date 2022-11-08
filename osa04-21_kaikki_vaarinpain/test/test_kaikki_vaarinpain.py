import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.kaikki_vaarinpain'
function = 'kaikki_vaarinpain'

def get_correct(test_case: list) -> list:
    return [x[::-1] for x in test_case][::-1]
@points('4.kaikki_vaarinpain')
class KaikkiVaarinpainTest(unittest.TestCase):
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
            from src.kaikki_vaarinpain import kaikki_vaarinpain
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä kaikki_vaarinpain(lista: list)')
        try:
            kaikki_vaarinpain = load(exercise, function, 'fi')
            kaikki_vaarinpain(["abc"])
        except:
            self.assertTrue(False, 'Varmista että seuraava funktiokutsu onnistuu kaikki_vaarinpain(["abc"])')

    def test_2_paluuarvon_tyyppi(self):
        kaikki_vaarinpain = load(exercise, function, 'fi')
        val = kaikki_vaarinpain(["abc"])
        self.assertTrue(type(val) == list, "Funktio kaikki_vaarinpain ei palauta listaa kutsuttaessa kaikki_vaarinpain(['abc'])")
    
    def test_3_lyhyet(self):
        for test_case in [["abc","def"], ["eka","toka","kolmas"], ["yksi","kaksi","kolme"]]:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                kaikki_vaarinpain = load(exercise, function, 'fi')
                
                correct = get_correct(test_case)
                test_case2 = test_case[:]
                test_result = kaikki_vaarinpain(test_case)

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa odotettua  {correct} kutsuttaessa kaikki_vaarinpain({test_case2})")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {test_case2} mutta se on {test_case}.")

    def test_4_pidemmat(self):
        for test_case in [["tässä", "on", "vähän", "pidempi", "lista", "jossa", "on", "useampia", "sanoja"],
                            ["abcd", "efghijklmnopqrstu", "vwxyz"]]:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                kaikki_vaarinpain = load(exercise, function, 'fi')
                
                correct = get_correct(test_case)
                test_case2 = test_case[:]
                test_result = kaikki_vaarinpain(test_case)

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa odotettua {correct} kaikki_vaarinpain({test_case2})kaikki_vaarinpain(")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {test_case2} mutta se on {test_case}.")
                
if __name__ == '__main__':
    unittest.main()
