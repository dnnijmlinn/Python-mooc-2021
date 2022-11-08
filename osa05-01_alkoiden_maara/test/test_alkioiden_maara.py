import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.alkioiden_maara'
function = 'laske_alkiot'

def get_correct(test_case: list, n: int) -> int:
    return reduce((lambda x,y: x + y), test_case).count(n)


@points('5.laske_alkiot')
class AlkioidenMaaraTest(unittest.TestCase):
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
            from src.alkioiden_maara import laske_alkiot
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä laske_alkiot(lista: list, alkio: int)' )
        try:
            from src.alkioiden_maara import laske_alkiot
            laske_alkiot([[1, 2]], 1)
        except:
            self.assertTrue(False, 'Tarkista että funktiota voi kutsua seuraavasti\nlaske_alkiot([[1, 2]], 1)' )

    def test_2_paluuarvon_tyyppi(self):
        laske_alkiot = load(exercise, function, 'fi')
        val = laske_alkiot([[1]], 1)
        self.assertTrue(type(val) == int, f"Funktio {function} ei palauta kokonaislukua parametrin arvoilla [[1]], 1.")
    
    def test_3_valmiit_matriisit(self):
        test_cases = (([[1,2,3],[2,3,1],[4,5,6]], 2), ([[1,5,5,3],[2,5,2,5],[0,0,2,5]], 5), ([[1,2,3,4],[2,3,4,5],[3,4,6,5]], 6))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                laske_alkiot = load(exercise, function, 'fi')
                
                correct = get_correct(test_case[0], test_case[1])
                test_case2 = test_case[0][:]
            
                try:
                    test_result = laske_alkiot(test_case[0], test_case[1])
                except:
                    self.assertTrue(False, f"Varmista että funktio toimii kun matriisi on {test_case[0]} ja etsittävä alkio {test_case[1]}")

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa mallivastausta {correct} kun matriisi on {test_case[0]} ja etsittävä alkio {test_case[1]}")
                self.assertEqual(test_case[0], test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {test_case2} mutta se on {test_case}.")

    def test_4_satunnaiset(self):
        for i in range(5):
            test_case = []
            length = randint(3,6)
            for j in range(randint(3,6)):
                test_case.append([randint(1,5) for i in range(length)])
            
            val = randint(1,5)

            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                laske_alkiot = load(exercise, function, 'fi')
                
                correct = get_correct(test_case, val)
                test_case2 = test_case[:]
        
                try:
                    test_result = laske_alkiot(test_case, val)
                except:
                    self.assertTrue(False, f"Varmista että funktio toimii kun matriisi on {test_case} ja etsittävä alkio {val}")


                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa mallivastausta {correct} kun matriisi on  {test_case} ja etsittävä alkio {val}.")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {test_case2} mutta se on {test_case}.")
              
if __name__ == '__main__':
    unittest.main()
