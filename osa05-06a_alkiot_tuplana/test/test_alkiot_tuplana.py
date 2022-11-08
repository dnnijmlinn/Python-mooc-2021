import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap
from random import randint

exercise = 'src.alkiot_tuplana'
function = 'tuplaa_alkiot'


@points('5.tuplaa_alkiot')
class TuplaaAlkiotTest(unittest.TestCase):
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
            from src.alkiot_tuplana import tuplaa_alkiot
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä tuplaa_alkiot(luvut: list)' )
        try:
            from src.alkiot_tuplana import tuplaa_alkiot
            tuplaa_alkiot([1])
        except:
            self.assertTrue(False, 'Tarkista että funktiota voi kutsua seuraavasti\ntuplaa_alkiot([1])' )

    def test_2_paluuarvon_tyyppi(self):
        tuplaa_alkiot = load(exercise, function, 'fi')
        val = tuplaa_alkiot([1])
        self.assertTrue(type(val) == list, f"Funktio {function} ei palauta listaa kutsulla tuplaa_alkiot([1]).")
    
    def test_3_listat(self):
        test_cases = ([1,3,5,7], [2,6,4,8,2,6,4], [9,7,5,3,1], [10,100,1000,100,10], [9,9,9,9,9])
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                output_alussa = get_stdout()
                tuplaa_alkiot = load(exercise, function, 'fi')
                
                correct = [x*2 for x in test_case]
                test_case2 = test_case[:]

                try:
                    test_result = tuplaa_alkiot(test_case)
                except:
                    self.assertTrue(False, f"Varmista että funktio toimii kun syöte on \n{test_case2}")

                self.assertEqual(correct, test_result, f"Tulos \n{test_result} \nei vastaa mallivastausta \n{correct} \nkun syöte on \n{test_case2}")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {test_case2} mutta se on {test_case}.")


              
if __name__ == '__main__':
    unittest.main()
