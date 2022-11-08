import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.positiivisten_summa'
function = 'positiivisten_summa'

def get_correct(test_case: list) -> list:
    return sum([x for x in test_case if x > 0])

@points('4.positiivisten_summa')
class PositiivistenSummaTest(unittest.TestCase):
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
            from src.positiivisten_summa import positiivisten_summa
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä positiivisten_summa(lista: list)')
        try:
            from src.positiivisten_summa import positiivisten_summa
            positiivisten_summa([1,2])
        except:
            self.assertTrue(False, 'Varmista että seuraava funktiokutsu onnistuu\npositiivisten_summa([1,2])')

    def test_2_paluuarvon_tyyppi(self):
        from src.positiivisten_summa import positiivisten_summa
        val = positiivisten_summa([1,2])
        self.assertTrue(type(val) == int, f"Funktio {function} ei palauta kokonaislukua kutsuttaessa positiivisten_summa([1,2])")
    
    def test_3_lukuja_1(self):
        test_cases = ([1,-1,2,-2,3,-3], [-9,-7,-5,-2,0,1,3,5,7,5], list(range(-10,10)))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                positiivisten_summa = load(exercise, function, 'fi')
                
                correct = get_correct(test_case)
                test_case2 = test_case[:]
                test_result = positiivisten_summa(list(test_case))

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa oikeaa vastausta {correct} kutsuttaessa positiivisten_summa({test_case2})")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {list(test_case2)} mutta se on {list(test_case)}.")

    def test_4_lukuja_2(self):
        test_cases = ([-10,-8,-6,-4,-2], [-100000,1,2,3,4,5], list(range(-1000,1000,100)))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                positiivisten_summa = load(exercise, function, 'fi')
                
                correct = get_correct(test_case)
                test_case2 = test_case[:]
                test_result = positiivisten_summa(list(test_case))

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa oikeaa vastausta {correct} testisyötteellä positiivisten_summa({test_case2})")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {list(test_case2)} mutta se on {list(test_case)}.")

    

    

    

    

    

   
    

    
              
if __name__ == '__main__':
    unittest.main()
