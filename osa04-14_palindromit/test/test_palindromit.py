import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout
from functools import reduce
import os
import textwrap

exercise = 'src.palindromit'
function = 'palindromi'

def get_correct(test_case: list) -> list:
    pass


@points('4.palindromit')
class PalindromitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["aa"]):
           cls.module = load_module(exercise, 'fi')

    def test_1_funktio_olemassa(self):
        try:
            from src.palindromit import palindromi
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä palindromi(sana: str)')
        try:
            from src.palindromit import palindromi
            palindromi("abba")
        except:
            self.assertTrue(False, 'Varmista että seuraava funktiokutsu onnistuu\npalindromi("abba")')

    def test_2_paluuarvon_tyyppi(self):
        from src.palindromit import palindromi
        val = palindromi("aa")
        self.assertTrue(type(val) == bool, f"Funktio {function} ei palauta totuusarvoa parametrin arvolla 'aa'.")
    
    def test_3_funktio(self):
        from src.palindromit import palindromi
        test_cases = {"abba" : True, "abccba" : True, "saippuakauppias" : True, "saippuakaupustelija" : False, "abbab": False, "abcabc" : False, "okok" : False}
        for test_case in test_cases:
            correct = test_cases[test_case]
            test_result = palindromi(test_case)

            self.assertTrue(correct == test_result, f'Funktion tulos {test_result} ei vastaa mallivastausta {correct} kutsuttaessa palindromi("{test_case}")')

    def test_4_syotteet(self):
        test_cases = "okei ei moikka moido mom".split()
        correct = ["ei ollut palindromi"] * 4
        correct.append("mom on palindromi!")
        
        with patch('builtins.input', side_effect=test_cases):
            reload_module(self.module)
            output = [x.strip().replace("  ", " ") for x in get_stdout().split("\n") if len(x.strip()) > 0]
            ncorrect = '\n'.join(correct)
            noutput = '\n'.join(output)

            ntest_cases = '\n'.join(test_cases)

            mssage = """\nHuomaa, että tässä tehtävässä mitään koodia EI TULE SIJOITTAA lohkon
if __name__ == "__main__":
sisälle
            """
            #\n{mssage}")   
            self.assertFalse(len(noutput)==0, f"Ohjelmasi ei tulosta mitään testisyötteellä\n{ntest_cases}\n{mssage}")
            self.assertTrue(correct == output, f"Tuloste\n{noutput}\nei vastaa mallivastausta:\n{ncorrect}\nseuraavalla testisyötteellä:\n{ntest_cases}")
     
if __name__ == '__main__':
    unittest.main()
