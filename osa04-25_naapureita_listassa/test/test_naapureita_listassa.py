import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
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

    def test_0_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test_1_funktio_olemassa(self):
        try:
            from src.naapureita_listassa import pisin_naapurijono
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä pisin_naapurijono(lista: list)')
        try:
            pisin_naapurijono([1,2])
        except:
            self.assertTrue(False, 'Varmista, että voit kutsua funktiota seuraavasti pisin_naapurijono([1, 2])')

    def test_2_paluuarvon_tyyppi(self):
        pisin_naapurijono = load(exercise, function, 'fi')
        val = pisin_naapurijono([1,2])
        self.assertTrue(type(val) == int, f"Funktio {function} ei palauta kokonaislukua parametrin arvolla [1,2].")
    
    def test_3_listat_1(self):
        test_cases = {(1,2,3,5,6,9,10): 3,
                      (0,2,4,5,6,7,10,11,12,100,101): 4,
                      (1,3,5,7,10,11,14,15,19,20,21,22,23,24,25,30): 7}
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

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa mallivastausta {correct} kutsuttaessa funktiota parametrilla {test_case2}.")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {list(test_case2)} mutta se on {list(test_case)}.")

if __name__ == '__main__':
    unittest.main()
