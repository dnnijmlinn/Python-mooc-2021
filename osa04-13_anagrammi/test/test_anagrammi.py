import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.anagrammi'
function = 'anagrammi'

def get_correct(s1 : str, s2: str) -> bool:
    pass

@points('4.anagrammi')
class AnagrammiTest(unittest.TestCase):
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
            from src.anagrammi import anagrammi
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä anagrammi(mjono1: str, mjono2: str)')
        try:
            from src.anagrammi import anagrammi
            anagrammi("olat","talo")
        except:
            self.assertTrue(False, 'Varmista että seuraava funktiokutsu onnistuu\nanagrammi("olat", "talo")')

    def test_2_paluuarvon_tyyppi(self):
        from src.anagrammi import anagrammi
        val = anagrammi("a","a")
        self.assertTrue(type(val) == bool, f"Funktio {function} ei palauta totuusarvoa parametrien arvoilla ('a', 'a').")
    
    def test_3_anagrammit(self):
        test_cases = [("talo","tola"), ("tuomi","muoti"), ("lattia","tilata"), ("testi","setti"), ("python","nythop")]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                from src.anagrammi import anagrammi
                
                correct = True
                test_result = anagrammi(test_case[0], test_case[1])

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa mallivastausta {correct} testisyötteellä {test_case}.")

    def test_4_ei_anagrammit(self):
        test_cases = [("talo","altto"), ("tuomi","muoto"), ("lattia","tilat"), ("testi","setsi"), ("python","java")]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                from src.anagrammi import anagrammi
                
                correct = False
                test_result = anagrammi(test_case[0], test_case[1])

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa mallivastausta {correct} testisyötteellä {test_case}.")
                



    

    

    
              
if __name__ == '__main__':
    unittest.main()
