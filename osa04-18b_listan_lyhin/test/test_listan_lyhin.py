import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import textwrap

exercise = 'src.listan_lyhin'
function = 'lyhin'

def get_correct(test_case: list) -> list:
    pass

@points('4.listan_lyhin')
class ListanPLyhinTest(unittest.TestCase):
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
            from src.listan_lyhin import lyhin
        except:
            self.assertTrue(False, 'Koodistasi pitäisi löytyä funktio nimeltä lyhin(lista: list)')
        try:
            lyhin = load(exercise, function, 'fi')
            lyhin(["abc", "ab"])
        except:
            self.assertTrue(False, 'Testaa funktiokutsu\nlyhin(["abc", "ab"])')

    def test_2_paluuarvon_tyyppi(self):
        lyhin = load(exercise, function, 'fi')
        val = lyhin(["Arto", "Matti"])
        self.assertTrue(type(val) == str, "Funktio lyhin ei palauta merkkijonoa parametrin arvolla ['Arto', 'Matti'].")
    
    def test_3_lyhin_loytyy(self):
        test_cases = {("Arto", "Leena", "Santeri", "Kim", "Minna") : ["Kim"], 
                      ("Jami", "Outi", "Magdalena", "Mia","Asko", "Toivo") : ["Mia"],
                      ("Serafiina", "Gandalf", "Harry", "Väiski") : ["Harry"]}
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                lyhin = load(exercise, function, 'fi')
                
                correct = test_cases[test_case][0]
                test_case2 = test_case[:]
                test_result = lyhin(list(test_case))

                self.assertEqual(correct, test_result, f"Tulos {test_result} ei vastaa odotettua {correct} kutsuttaessa lyhin{test_case2}")
                self.assertEqual(test_case, test_case2, f"Funktio ei saa muuttaa alkuperäistä listaa. Arvon pitäisi olla {list(test_case2)} mutta se on {list(test_case)}.")

if __name__ == '__main__':
    unittest.main()
