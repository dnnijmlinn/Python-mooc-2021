import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.go'
function = 'kumpi_voitti'

def get_correct(test_case: list) -> int:
    c = [(reduce((lambda x,y: x + y), test_case).count(n), n) for n in (1,2)]
    return max(c)[1] if c[0][0] != c[1][0] else 0


@points('5.go')
class GoTest(unittest.TestCase):
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
            from src.go import kumpi_voitti
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä kumpi_voitti(pelilauta: list)')
        try:
            kumpi_voitti = load(exercise, function, 'fi')
            kumpi_voitti([[1]])
        except:
            self.assertTrue(False, 'Tarkista että funktiota voi kutsua seuraavasti\nkumpi_voitti([[1]])')

    def test_2_paluuarvon_tyyppi(self):
        kumpi_voitti = load(exercise, function, 'fi')
        val = kumpi_voitti([[1]])
        self.assertTrue(type(val) == int, f"Funktio {function} ei palauta kokonaislukua parametrin arvoilla [[1]], 1.")
    
    def test_3_valmiit_laudat(self):
        test_cases = (([[1,2,1],[0,0,1],[2,1,0]], 1), ([[1,2,2,2],[0,0,0,1],[0,0,2,1]], 2), ([[1,2,2,2],[2,1,1,1],[0,2,1,0]], 0))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                kumpi_voitti = load(exercise, function, 'fi')
                
                correct = test_case[1]
                test_case2 = test_case[0][:]
                try:
                    test_result = kumpi_voitti(test_case[0])
                except:
                    self.assertTrue(False, f"Varmista että funktio toimii kun matriisi on {test_case[0]}")

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa mallivastausta {correct} kun matriisi on {test_case[0]}")
                self.assertEqual(test_case[0], test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {test_case2} mutta se on {test_case[0]}.")

    def test_4_satunnaiset_laudat(self):
        for i in range(5):
            test_case = []
            length = randint(5,10)
            for j in range(length):
                test_case.append([randint(0,2) for x in range(length)])
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                kumpi_voitti = load(exercise, function, 'fi')
                
                correct = get_correct(test_case)
                test_case2 = test_case
                try:
                    test_result = kumpi_voitti(test_case)
                except:
                    self.assertTrue(False, f"Varmista että funktio toimii kun matriisi on {test_case}")

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa mallivastausta {correct} kun matriisi on \n{test_case}")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {test_case2} mutta se on {test_case}.")
       
if __name__ == '__main__':
    unittest.main()
